from pymodbus.client import ModbusTcpClient

def getClient(host:str = "192.168.11.210",port = 6000) -> ModbusTcpClient:
    client = ModbusTcpClient(host=host,port=port,timeout=3)
    if not client.connect():
        print("连接失败！检查设备IP/端口是否正确")
        exit()
    return client

if __name__ == "__main__":
    client = getClient()