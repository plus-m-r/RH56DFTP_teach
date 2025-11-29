from abc import ABC, abstractmethod
from Register.RegisterKey.ftp_registers_keys import RegisterName

class RH56DFTP_base(ABC):
    """
    RH56DFTP 基类，定义了设备通信的基本接口
    """
    
    @classmethod
    @abstractmethod
    def __init__(cls, host: str, port: int) -> None:
        """
        初始化连接
        
        Args:
            host: 设备IP地址
            port: 设备端口号
        """
        ...
    
    @classmethod
    @abstractmethod
    def get(cls, register_name: RegisterName) -> any:
        """
        获取指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            
        Returns:
            寄存器的当前值
        """
        ...
    
    @classmethod
    @abstractmethod
    def set(cls, register_name: RegisterName, value: any) -> bool:
        """
        设置指定寄存器的值
        
        Args:
            register_name: 寄存器名称
            value: 要设置的值
            
        Returns:
            设置是否成功
        """
        ...
    
    @classmethod
    @abstractmethod
    def _check_connect(cls) -> bool:
        """
        检查连接是否正常
        
        Returns:
            连接是否正常
        """
        ...
