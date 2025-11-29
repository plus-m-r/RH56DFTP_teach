"""
RH56DFTP 基类模块，定义了设备通信的基本接口
"""
from abc import ABC, abstractmethod
from Register.RegisterKey.ftp_registers_keys import RegisterName

class RH56DFTPBase(ABC):
    """
    RH56DFTP 基类，后期可以根据协议不同而重写
    """
    @abstractmethod
    def __init__(self, host: str, port: int, config_folder_path: str = "Register/config/configFTP"):
        """
        初始化连接在这里完成

        Args:
            host: 设备IP地址
            port: 设备端口号
            config_folder_path: 寄存器配置文件夹路径
        """

    @abstractmethod
    def get(self, register_name: RegisterName) -> any:
        """
        获取指定寄存器的值

        Args:
            register_name: 寄存器名称，使用RegisterName类型提供编码提示

        Returns:
            寄存器的当前值
        """

    @abstractmethod
    def set(self, register_name: RegisterName, value: any) -> bool:
        """
        设置指定寄存器的值

        Args:
            register_name: 寄存器名称，使用RegisterName类型提供编码提示
            value: 要设置的值

        Returns:
            设置是否成功
        """

    @abstractmethod
    def _check_connect(self) -> bool:
        """
        每次使用set与get时检查连接,默认set与get为低频操作，有性能要求加入另外的get,set.

        Returns:
            连接是否正常
        """
