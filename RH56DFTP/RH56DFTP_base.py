from abc import ABC,abstractmethod
from Register.RegisterSet.Register_FTP import Register_FTP

class RegisterAdress:
    def __init__(self):
        class base:
            def __init__(self):
                self.HAND_ID = 1000
                self.REDU_RATIO = 1002
                self.CLEAR_ERROR = 1004
                self.SAVE = 1005
                self.RESET_PARA = 1006
                self.GESTURE_FORCE_CLB = 1009
        class set:
            def __init__(self):
                self.DEFAULT_SPEED_SET = 1032
                self.DEFAULT_FORCE_SET = 1044
                self.POS_SET = 1474
                self.ANGLE_SET = 1486
                self.FORCE_SET = 1498
                self.SPEED_SET = 1522
        class act:
            def __init__(self):
                self.POS_ACT = 1534
                self.ANGLE_ACT = 1546
                self.FORCE_ACT = 1582
                self.CURRENT = 1594
                self.ERROR = 1606
                self.STATUS = 1612
                self.TEMP = 1618
        class IP:
            def __init__(self):
                self.IP_PART1 = 1700
                self.IP_PART2 = 1701
                self.IP_PART3 = 1702
                self.IP_PART4 = 1703
        class TOUCH:
            def __init__(self):
                self.FINGERONE_TOUCH = 3000
                self.FINGERTWO_TOUCH = 3370
                self.FINGERTHE_TOUCH = 3740
                self.FINGERFOR_TOUCH = 4110
                self.FINGERFIV_TOUCH = 4480
                self.FINGERPALM_TOUCH = 4900

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
        super.__init__()
        pass
    @classmethod
    @abstractmethod
    def get(cls,Register_FTP):
        """
        获取各种寄存器有用值
        """
        pass
    @classmethod
    @abstractmethod
    def set(cls,Register_FTP):
        """
        设置各种寄存器值，并有coding时提示
        """
        pass
    @classmethod
    @abstractmethod
    def _check_connect():
        """
        每次使用set与get时检查连接,默认set与get为低频操作，有性能要求加入另外的get,set.
        """
        pass