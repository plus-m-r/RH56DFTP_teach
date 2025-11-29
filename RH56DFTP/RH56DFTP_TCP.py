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

    def __init__(self, host: str, port: int, config_folder_path: str = "Register/config/configFTP"):
        """
        初始化TCP连接

        Args:
            host: 设备IP地址
            port: 设备端口号
            config_folder_path: 寄存器配置文件夹路径，默认为 "Register/config/configFTP"

        Raises:
            ConnectionError: 当连接失败时抛出
        """
        logger.info("正在初始化连接到设备: %s:%s", host, port)
        self.client = ModbusTcpClient(host=host, port=port, timeout=3)
        if not self.client.connect():
            logger.error("连接失败：无法连接到 %s:%s", host, port)
            raise ConnectionError(f"连接失败：无法连接到 {host}:{port}")

        # 创建寄存器对象字典
        logger.debug("正在创建寄存器对象字典，配置路径: %s", config_folder_path)
        self.registers: Dict[RegisterName, Register_FTP] = register_factory.create_registers(
            config_folder_path=config_folder_path,
            strategy_name='ftp'
        )
        logger.info("成功连接到 %s:%s", host, port)
        logger.info("已加载 %d 个寄存器", len(self.registers))

    def get(self, register_name: RegisterName) -> Any:
        """
        获取指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            
        Returns:
            寄存器的当前值
        
        Raises:
            ValueError: 当寄存器不存在或读取失败时抛出
        """
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
        value = None

        try:
            # 根据地址类型处理
            if isinstance(register.address, int):
                # 单个地址
                logger.debug("读取单个地址寄存器 %s，地址: %d", register_name, register.address)
                response = self.client.read_holding_registers(
                    address=register.address,
                    count=1  # 假设大多数寄存器是1个寄存器
                )
                if response.isError():
                    logger.error("读取寄存器 %s 失败: %s", register_name, response)
                    raise ValueError(f"读取寄存器 {register_name} 失败: {response}")
                value = response.registers[0]
                logger.info("成功读取寄存器 %s: 值=%d, 地址=%d", register_name, value, register.address)
            elif isinstance(register.address, tuple) and len(register.address) == 2:
                # 地址范围
                start_address, end_address = register.address
                count = end_address - start_address + 1
                logger.debug("读取地址范围寄存器 %s，地址范围: %d-%d, 数量: %d",
                            register_name, start_address, end_address, count)
                response = self.client.read_holding_registers(
                    address=start_address,
                    count=count
                )
                if response.isError():
                    logger.error("读取寄存器 %s 失败: %s", register_name, response)
                    raise ValueError(f"读取寄存器 {register_name} 失败: {response}")

                # 根据数据类型进行解析
                if register.data_type == "short" and count == 2:
                    # 2字节数据，可能需要处理高低字节
                    value = response.registers[0]  # 简化处理，实际可能需要合并
                    logger.info("成功读取寄存器 %s: 值=%d, 地址范围=%d-%d",
                               register_name, value, start_address, end_address)
                else:
                    value = response.registers
                    logger.info("成功读取寄存器 %s: 值=%s, 地址范围=%d-%d",
                               register_name, value, start_address, end_address)
            else:
                # 无效地址格式
                logger.error("读取寄存器 %s 失败: 无效的地址格式 %s", register_name, register.address)
                raise ValueError(f"无效的地址格式: {register.address}")

        except Exception as e:
            logger.error("读取寄存器 %s 时出错: %s", register_name, str(e))
            raise ValueError(f"读取寄存器 {register_name} 时出错: {str(e)}") from e

        return value

    def set(self, register_name: RegisterName, value: Any) -> bool:
        """
        设置指定寄存器的值

        Args:
            register_name: 寄存器名称
            value: 要设置的值

        Returns:
            设置是否成功
        """
        logger.info("开始设置寄存器: %s, 值: %s", register_name, value)

        if not self._check_connect():
            logger.error("设置寄存器 %s 失败: 连接已断开", register_name)
            return False

        if register_name not in self.registers:
            logger.error("设置寄存器 %s 失败: 寄存器不存在", register_name)
            return False

        register = self.registers[register_name]

        # 检查访问权限
        if register.access_type == "read-only":
            logger.error("设置寄存器 %s 失败: 寄存器是只读的", register_name)
            return False

        try:
            # 检查值范围
            if isinstance(register.value_range, tuple) and len(register.value_range) == 2:
                min_val, max_val = register.value_range
                if not min_val <= value <= max_val:
                    logger.error("设置寄存器 %s 失败: 值 %s 超出范围 [%s, %s]",
                                register_name, value, min_val, max_val)
                    return False

            # 根据地址类型处理
            if isinstance(register.address, int):
                logger.debug("写入单个地址寄存器 %s，地址: %d, 值: %s",
                            register_name, register.address, value)
                response = self.client.write_register(
                    address=register.address,
                    value=int(value)  # 假设需要转换为整数
                )
                if response.isError():
                    logger.error("设置寄存器 %s 失败: %s", register_name, response)
                    return False
                logger.info("成功设置寄存器 %s: 值=%s, 地址=%d",
                           register_name, value, register.address)
                return True

            # 处理多寄存器写入
            if isinstance(register.address, tuple) and len(register.address) == 2:
                start_address = register.address[0]
                logger.debug("写入地址范围寄存器 %s，起始地址: %d, 值: %s",
                            register_name, start_address, value)

                if isinstance(value, int):
                    response = self.client.write_register(
                        address=start_address,
                        value=value
                    )
                    if response.isError():
                        logger.error("设置寄存器 %s 失败: %s", register_name, response)
                        return False
                    logger.info("成功设置寄存器 %s: 值=%s, 起始地址=%d",
                               register_name, value, start_address)
                    return True

                logger.error("设置寄存器 %s 失败: 不支持的值类型 %s",
                            register_name, type(value))
                return False

            logger.error("设置寄存器 %s 失败: 无效的地址格式 %s",
                        register_name, register.address)
            return False

        except (ValueError, TypeError) as e:
            logger.error("设置寄存器 %s 时出错: %s", register_name, str(e))
            return False
        except (ConnectionError, TimeoutError, OSError) as e:
            logger.error("设置寄存器 %s 时发生连接错误: %s", register_name, str(e))
            return False

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
