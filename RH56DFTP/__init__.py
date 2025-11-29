"""
RH56DFTP 库，用于通过Modbus TCP协议与RH56DFTP设备通信
"""

from .RH56DFTP_base import RH56DFTPBase
from .RH56DFTP_TCP import RH56DFTPClient

__all__ = [
    "RH56DFTPBase",
    "RH56DFTPClient"
]
__version__ = "0.1.0"
