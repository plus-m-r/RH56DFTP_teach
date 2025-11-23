from abc import ABC, abstractmethod
from Register.RegisterKey.ftp_registers_keys import RegisterName

class RH56DFTP_base(ABC):
    """
        RH56DFTP 基类，后期可以根据协议不同而重写，因为我只想写TCP
    """
    @classmethod
    @abstractmethod
    def __init__(cls):
        """
        初始化连接在这里完成
        """
        super().__init__()
        pass
    
    @classmethod
    @abstractmethod
    def get(cls, register_name: RegisterName) -> any:
        """
        获取指定寄存器的值
        
        Args:
            register_name: 寄存器名称，使用RegisterName类型提供编码提示
            
        Returns:
            寄存器的当前值
        """
        pass
    
    @classmethod
    @abstractmethod
    def set(cls, register_name: RegisterName, value: any) -> bool:
        """
        设置指定寄存器的值
        
        Args:
            register_name: 寄存器名称，使用RegisterName类型提供编码提示
            value: 要设置的值
            
        Returns:
            设置是否成功
        """
        pass
    
    @classmethod
    @abstractmethod
    def _check_connect(cls) -> bool:
        """
        每次使用set与get时检查连接,默认set与get为低频操作，有性能要求加入另外的get,set.
        
        Returns:
            连接是否正常
        """
        pass
    