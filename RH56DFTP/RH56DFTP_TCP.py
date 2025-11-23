from .RH56DFTP_base import RH56DFTP_base
from pymodbus.client import ModbusTcpClient
from Register.RegisterKey.ftp_registers_keys import RegisterName
from Register.RegisterBuild.RegisterFactory import register_factory
from Register.RegisterSet.Register_FTP import Register_FTP
from typing import Any, Dict

class RH56DFTP_TCP(RH56DFTP_base):
    """
    RH56DFTP的TCP实现类，用于通过Modbus TCP协议与设备通信
    """
    
    def __init__(self, host: str, port: int):
        """
        初始化TCP连接
        
        Args:
            host: 设备IP地址
            port: 设备端口号
        
        Raises:
            ConnectionError: 当连接失败时抛出
        """
        self.client = ModbusTcpClient(host=host, port=port, timeout=3)
        if not self.client.connect():
            raise ConnectionError(f"连接失败：无法连接到 {host}:{port}")
        
        # 创建寄存器对象字典
        self.registers: Dict[RegisterName, Register_FTP] = register_factory.create_registers(
            config_folder_path="Register/config/configFTP", 
            strategy_name='ftp'
        )
        print(f"成功连接到 {host}:{port}")
    
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
        if not self._check_connect():
            raise ConnectionError("连接已断开")
        
        if register_name not in self.registers:
            raise ValueError(f"寄存器 {register_name} 不存在")
        
        register = self.registers[register_name]
        
        try:
            # 根据地址类型处理
            if isinstance(register.address, int):
                # 单个地址
                response = self.client.read_holding_registers(
                    address=register.address, 
                    count=1  # 假设大多数寄存器是1个寄存器
                )
                if response.isError():
                    raise ValueError(f"读取寄存器 {register_name} 失败: {response}")
                return response.registers[0]
            elif isinstance(register.address, tuple) and len(register.address) == 2:
                # 地址范围
                start_address, end_address = register.address
                count = end_address - start_address + 1
                response = self.client.read_holding_registers(
                    address=start_address, 
                    count=count
                )
                if response.isError():
                    raise ValueError(f"读取寄存器 {register_name} 失败: {response}")
                # 根据数据类型进行解析
                if register.data_type == "short":
                    # 2字节数据，可能需要处理高低字节
                    if count == 2:
                        return response.registers[0]  # 简化处理，实际可能需要合并
                return response.registers
            else:
                raise ValueError(f"无效的地址格式: {register.address}")
                
        except Exception as e:
            raise ValueError(f"读取寄存器 {register_name} 时出错: {str(e)}")
    
    def set(self, register_name: RegisterName, value: Any) -> bool:
        """
        设置指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            value: 要设置的值
            
        Returns:
            设置是否成功
        """
        if not self._check_connect():
            print("连接已断开")
            return False
        
        if register_name not in self.registers:
            print(f"寄存器 {register_name} 不存在")
            return False
        
        register = self.registers[register_name]
        
        # 检查访问权限
        if register.access_type == "read-only":
            print(f"寄存器 {register_name} 是只读的")
            return False
        
        try:
            # 检查值范围
            if isinstance(register.value_range, tuple) and len(register.value_range) == 2:
                min_val, max_val = register.value_range
                if not (min_val <= value <= max_val):
                    print(f"值 {value} 超出范围 [{min_val}, {max_val}]")
                    return False
            
            # 根据地址类型处理
            if isinstance(register.address, int):
                response = self.client.write_register(
                    address=register.address, 
                    value=int(value)  # 假设需要转换为整数
                )
                return not response.isError()
            elif isinstance(register.address, tuple) and len(register.address) == 2:
                # 处理多寄存器写入
                start_address = register.address[0]
                # 简化处理，实际可能需要根据数据类型转换
                if isinstance(value, int):
                    response = self.client.write_register(
                        address=start_address, 
                        value=value
                    )
                    return not response.isError()
                else:
                    print(f"不支持的值类型: {type(value)}")
                    return False
            else:
                print(f"无效的地址格式: {register.address}")
                return False
                
        except Exception as e:
            print(f"设置寄存器 {register_name} 时出错: {str(e)}")
            return False
    
    def _check_connect(self) -> bool:
        """
        检查连接是否正常
        
        Returns:
            连接是否正常
        """
        if self.client is None:
            return False
        
        # 尝试发送一个简单的命令来验证连接
        try:
            # 使用一个不会改变设备状态的简单读取操作
            # 这里使用0地址作为示例，实际应用中可能需要使用一个安全的地址
            response = self.client.read_holding_registers(address=0, count=1)
            return not response.isError()
        except:
            # 如果连接断开，尝试重新连接
            try:
                self.client.close()
                return self.client.connect()
            except:
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
    
    def close(self):
        """
        关闭连接
        """
        if self.client:
            self.client.close()
            print("连接已关闭")
    
    def __del__(self):
        """
        析构函数，确保连接被关闭
        """
        self.close()