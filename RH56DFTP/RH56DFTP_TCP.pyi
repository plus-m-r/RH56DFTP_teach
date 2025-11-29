from typing import Any, Dict
from .RH56DFTP_base import RH56DFTP_base
from Register.RegisterKey.ftp_registers_keys import RegisterName
from Register.RegisterSet.Register_FTP import Register_FTP
from pymodbus.client import ModbusTcpClient

class RH56DFTP_TCP(RH56DFTP_base):
    """
    RH56DFTP的TCP实现类，用于通过Modbus TCP协议与设备通信
    """
    
    client: ModbusTcpClient
    registers: Dict[RegisterName, Register_FTP]
    
    def __init__(self, host: str, port: int) -> None:
        """
        初始化TCP连接
        
        Args:
            host: 设备IP地址
            port: 设备端口号
        
        Raises:
            ConnectionError: 当连接失败时抛出
        """
        ...
    
    def get(self, register_name: RegisterName) -> Any:
        """
        获取指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            
        Returns:
            寄存器的当前值
        
        Raises:
            ValueError: 当寄存器不存在或读取失败时抛出
            ConnectionError: 当连接已断开时抛出
        """
        ...
    
    def set(self, register_name: RegisterName, value: Any) -> bool:
        """
        设置指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            value: 要设置的值
            
        Returns:
            设置是否成功
        """
        ...
    
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
        ...
    
    def _check_connect(self) -> bool:
        """
        检查连接是否正常
        
        Returns:
            连接是否正常
        """
        ...
    
    def close(self) -> None:
        """
        关闭连接
        """
        ...
    
    def __del__(self) -> None:
        """
        析构函数，确保连接被关闭
        """
        ...
