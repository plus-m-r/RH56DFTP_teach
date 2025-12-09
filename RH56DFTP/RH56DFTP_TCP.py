"""
RH56DFTP TCP实现模块，用于通过Modbus TCP协议与设备通信
"""
# 标准库导入
import logging
from typing import Any, Dict

# 第三方库导入
from pymodbus.client import ModbusTcpClient

# 本地库导入
from Register.RegisterKey.ftp_registers_keys import RegisterName
from Register.RegisterBuild.RegisterFactory import register_factory
from Register.RegisterSet.Register_FTP import Register_FTP
from .RH56DFTP_base import RH56DFTPBase

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rh56dftp.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('RH56DFTP')

class RH56DFTPClient(RH56DFTPBase):
    """
    RH56DFTP的TCP实现类，用于通过Modbus TCP协议与设备通信
    """

    def __init__(self, host: str, port: int, config_folder_path: str = None):
        """
        初始化TCP连接

        Args:
            host: 设备IP地址
            port: 设备端口号
            config_folder_path: 寄存器配置文件夹路径，默认为包内的配置路径

        Raises:
            ConnectionError: 当连接失败时抛出
        """
        logger.info("正在初始化连接到设备: %s:%s", host, port)
        self.client = ModbusTcpClient(host=host, port=port, timeout=3)
        self.is_connected = self.client.connect()
        
        if not self.is_connected:
            logger.warning("连接失败：无法连接到 %s:%s，将以离线模式初始化", host, port)
        else:
            logger.info("成功连接到 %s:%s", host, port)

        # 创建寄存器对象字典
        logger.debug("正在创建寄存器对象字典，使用内置配置")
        self.registers: Dict[RegisterName, Register_FTP] = register_factory.create_registers(
            config_folder_path=None,
            strategy_name='ftp'
        )
        
        # 动态注入寄存器方法，用于IDE函数提示
        logger.debug("正在动态注入寄存器方法")
        for register_name in self.registers:
            register = self.registers[register_name]
            # 创建一个闭包，捕获当前寄存器名称
            def create_getter(r_name, r_data_type, r_address, r_access_type, r_description):
                # 定义动态方法
                def getter():
                    """动态生成的寄存器读取方法"""
                    if not self.is_connected:
                        raise ConnectionError("设备未连接")
                    return self.get(r_name)
                # 设置方法名称
                getter.__name__ = f"get_{r_name}"
                # 设置文档字符串
                getter.__doc__ = f"获取寄存器 {r_name} 的值\n\n" + \
                                f"地址: {r_address}\n" + \
                                f"数据类型: {r_data_type}\n" + \
                                f"访问类型: {r_access_type}\n" + \
                                f"描述: {r_description}"
                # 添加返回类型注解
                # 根据数据类型设置返回类型
                if r_data_type == "uint8":
                    getter.__annotations__["return"] = int
                elif r_data_type == "short":
                    getter.__annotations__["return"] = int
                else:
                    getter.__annotations__["return"] = Any
                return getter
            
            # 生成并添加方法到实例
            getter_method = create_getter(
                register_name, 
                register.data_type, 
                register.address, 
                register.access_type, 
                register.description
            )
            setattr(self, f"get_{register_name}", getter_method)
        
        logger.info("已加载 %d 个寄存器，动态注入了 %d 个方法", len(self.registers), len(self.registers))

    def _process_raw_value(self, register, raw_value):
        """处理原始寄存器值，根据数据类型转换"""
        if register.data_type == "uint8":
            # uint8类型，只取低8位
            return raw_value & 0xFF
        if register.data_type == "short":
            # short类型，处理16位有符号值
            return raw_value - 65536 if raw_value > 32767 else raw_value
        return raw_value

    def _read_single_register(self, register, register_name):
        """读取单个寄存器"""
        logger.debug("读取单个地址寄存器 %s，地址: %d", register_name, register.address)
        response = self.client.read_holding_registers(
            address=register.address,
            count=1  # 单个寄存器（16位）
        )
        if response.isError():
            logger.error("读取寄存器 %s 失败: %s", register_name, response)
            raise ValueError(f"读取寄存器 {register_name} 失败: {response}")
        raw_value = response.registers[0]
        value = self._process_raw_value(register, raw_value)
        logger.info("成功读取寄存器 %s: 值=%d, 地址=%d", register_name, value, register.address)
        return value

    def _read_register_batch(self, start_address, count):
        """读取寄存器批次"""
        max_count_per_read = 125
        all_registers = []
        current_addr = start_address
        remaining = count

        while remaining > 0:
            batch_count = min(remaining, max_count_per_read)
            logger.debug("读取批次: 起始地址=%d, 数量=%d, 剩余=%d",
                        current_addr, batch_count, remaining - batch_count)

            response = self.client.read_holding_registers(
                address=current_addr,
                count=batch_count
            )
            if response.isError():
                raise ValueError(f"读取寄存器失败: {response}")

            all_registers.extend(response.registers)
            current_addr += batch_count
            remaining -= batch_count

        return all_registers

    def _read_range_register(self, register, register_name):
        """读取地址范围寄存器"""
        start_address, end_address = register.address
        count = end_address - start_address + 1
        logger.debug("读取地址范围寄存器 %s，地址范围: %d-%d, 数量: %d",
                    register_name, start_address, end_address, count)

        all_registers = self._read_register_batch(start_address, count)

        # 根据数据类型进行解析
        if register.data_type == "short" and count == 2:
            raw_value = all_registers[0]
            value = self._process_raw_value(register, raw_value)
            logger.info("成功读取寄存器 %s: 值=%d, 地址范围=%d-%d",
                       register_name, value, start_address, end_address)
        else:
            value = all_registers
            logger.info("成功读取寄存器 %s: 值=%s, 地址范围=%d-%d",
                       register_name, value, start_address, end_address)
        return value

    def get(self, register_name: RegisterName | callable) -> Any:
        """
        获取指定寄存器的值

        Args:
            register_name: 寄存器名称或寄存器函数对象

        Returns:
            寄存器的当前值

        Raises:
            ValueError: 当寄存器不存在或读取失败时抛出
        """
        # 处理函数对象，提取函数名称作为寄存器名称
        original_register_name = register_name
        if callable(register_name):
            # 从REGISTE_MAP中查找对应的寄存器名称
            found_name = None
            for name, func in self.registers.items():
                func_name = name.replace("(", "_").replace(")", "")
                if register_name.__name__ == func_name:
                    found_name = name
                    break
            if found_name:
                register_name = found_name
            else:
                register_name = register_name.__name__
        
        logger.info("开始读取寄存器: %s", register_name)

        # 检查连接状态
        if not self._check_connect():
            logger.error("读取寄存器 %s 失败: 连接已断开", register_name)
            raise ConnectionError("连接已断开")

        # 检查寄存器是否存在
        if register_name not in self.registers:
            logger.error("读取寄存器 %s 失败: 寄存器不存在", register_name)
            raise ValueError(f"寄存器 {register_name} 不存在")

        register = self.registers[register_name]

        try:
            # 根据地址类型处理
            if isinstance(register.address, int):
                return self._read_single_register(register, register_name)
            if isinstance(register.address, tuple) and len(register.address) == 2:
                return self._read_range_register(register, register_name)
            # 无效地址格式
            logger.error("读取寄存器 %s 失败: 无效的地址格式 %s", register_name, register.address)
            raise ValueError(f"无效的地址格式: {register.address}")

        except Exception as e:
            logger.error("读取寄存器 %s 时出错: %s", register_name, str(e))
            raise ValueError(f"读取寄存器 {register_name} 时出错: {str(e)}") from e

    def set(self, register_name: RegisterName | callable, value: Any) -> bool:
        """
        设置指定寄存器的值

        Args:
            register_name: 寄存器名称或寄存器函数对象
            value: 要设置的值

        Returns:
            设置是否成功
        """
        # 处理函数对象，提取函数名称作为寄存器名称
        if callable(register_name):
            # 从REGISTE_MAP中查找对应的寄存器名称
            found_name = None
            for name, func in self.registers.items():
                func_name = name.replace("(", "_").replace(")", "")
                if register_name.__name__ == func_name:
                    found_name = name
                    break
            if found_name:
                register_name = found_name
            else:
                register_name = register_name.__name__
        
        logger.info("开始设置寄存器: %s, 值: %s", register_name, value)

        # 1. 检查连接状态
        if not self._check_connect():
            logger.error("设置寄存器 %s 失败: 连接已断开", register_name)
            return False

        # 2. 检查寄存器是否存在
        if register_name not in self.registers:
            logger.error("设置寄存器 %s 失败: 寄存器不存在", register_name)
            return False

        register = self.registers[register_name]

        # 3. 检查访问权限
        if register.access_type == "read-only":
            logger.error("设置寄存器 %s 失败: 寄存器是只读的", register_name)
            return False

        # 4. 检查值范围
        if isinstance(register.value_range, tuple) and len(register.value_range) == 2:
            min_val, max_val = register.value_range
            if not min_val <= value <= max_val:
                logger.error("设置寄存器 %s 失败: 值 %s 超出范围 [%s, %s]",
                            register_name, value, min_val, max_val)
                return False

        # 5. 处理写入操作
        return self._write_register(register, value)

    def _write_register(self, register: Register_FTP, value: Any) -> bool:
        """
        执行寄存器写入操作
        
        Args:
            register: 寄存器对象
            value: 要写入的值
            
        Returns:
            写入是否成功
        """
        success = False

        try:
            # 处理负数，转换为对应的无符号值
            write_value = int(value)
            # 如果是负数，转换为对应的无符号16位整数
            if write_value < 0:
                write_value = 65536 + write_value
                logger.debug("将负数 %d 转换为无符号值 %d", int(value), write_value)

            # 单个地址写入
            if isinstance(register.address, int):
                logger.debug("写入单个地址寄存器 %s，地址: %d, 值: %s, 转换后值: %d",
                            register.name, register.address, value, write_value)
                response = self.client.write_register(
                    address=register.address,
                    value=write_value
                )
                if not response.isError():
                    logger.info("成功设置寄存器 %s: 值=%s, 地址=%d",
                               register.name, value, register.address)
                    success = True
                else:
                    logger.error("设置寄存器 %s 失败: %s", register.name, response)
            # 地址范围写入
            elif isinstance(register.address, tuple) and len(register.address) == 2:
                start_address = register.address[0]
                logger.debug("写入地址范围寄存器 %s，起始地址: %d, 值: %s, 转换后值: %d",
                            register.name, start_address, value, write_value)

                response = self.client.write_register(
                    address=start_address,
                    value=write_value
                )
                if not response.isError():
                    logger.info("成功设置寄存器 %s: 值=%s, 起始地址=%d",
                               register.name, value, start_address)
                    success = True
                else:
                    logger.error("设置寄存器 %s 失败: %s", register.name, response)
            # 无效地址格式
            else:
                logger.error("设置寄存器 %s 失败: 无效的地址格式 %s",
                            register.name, register.address)
        except (ValueError, TypeError) as e:
            logger.error("设置寄存器 %s 时出错: %s", register.name, str(e))
        except (ConnectionError, TimeoutError, OSError) as e:
            logger.error("设置寄存器 %s 时发生连接错误: %s", register.name, str(e))

        return success

    def _check_connect(self) -> bool:
        """
        检查连接是否正常
        
        Returns:
            连接是否正常
        """
        if self.client is None:
            logger.error("连接检查失败: 客户端对象为None")
            return False

        def _attempt_reconnect() -> bool:
            """尝试重新连接设备"""
            try:
                self.client.close()
                if self.client.connect():
                    logger.info("连接已成功重新建立")
                    return True
                logger.error("连接检查失败: 无法重新连接到设备")
                return False
            except (ConnectionError, TimeoutError, OSError) as re:
                logger.error("连接检查失败: 重新连接时发生错误: %s", str(re))
                return False

        # 尝试发送一个简单的命令来验证连接
        try:
            # 使用一个不会改变设备状态的简单读取操作
            # 这里使用0地址作为示例，实际应用中可能需要使用一个安全的地址
            response = self.client.read_holding_registers(address=0, count=1)
            return not response.isError()
        except (ConnectionError, TimeoutError, OSError) as e:
            logger.warning("连接检查失败: %s，尝试重新连接", str(e))
            return _attempt_reconnect()
        except (AttributeError, ValueError) as e:
            logger.error("连接检查失败: 客户端对象异常: %s", str(e))
            return False

    def get_register(self, register_name: RegisterName) -> Register_FTP:
        """
        获取寄存器对象

        Args:
            register_name: 寄存器名称

        Returns:
            对应的Register_FTP对象

        Raises:
            ValueError: 当寄存器不存在时抛出
        """
        if register_name not in self.registers:
            raise ValueError(f"寄存器 {register_name} 不存在")
        return self.registers[register_name]

    def close(self) -> None:
        """
        关闭连接
        """
        if self.client:
            logger.info("正在关闭连接")
            self.client.close()
            logger.info("连接已关闭")

    def __del__(self) -> None:
        """
        析构函数，确保连接被关闭
        """
        self.close()

# 添加别名以保持向后兼容
RH56DFTP_TCP = RH56DFTPClient  # pylint: disable=invalid-name
