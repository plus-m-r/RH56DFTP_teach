from RH56DFTP_base import RH56DFTP_base , RegisterAdress
from pymodbus.client import ModbusTcpClient

class RH56DFTP_TCP(RH56DFTP_base):
    def __init__(self,host : str,port : int):
        self.client = ModbusTcpClient(host = host,port = port,timeout=3)
        if not self.client.connect():
            raise "连接失败，退出"
            exit()
    def get(register):
