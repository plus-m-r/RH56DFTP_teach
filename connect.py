from pymodbus.client import ModbusTcpClient
import socket
import ipaddress
import concurrent.futures

def getClient(host="192.168.123.210", port=6000, timeout=3.0):
    try:
        client = ModbusTcpClient(host=host, port=port, timeout=timeout)
        if client.connect():
            print(f"成功连接到Modbus设备: {host}:{port}")
            return client
        client.close()
    except: pass
    return None

if __name__ == "__main__":
    client = getClient()