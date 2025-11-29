from typing import Tuple, Union
from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterBase:
    """
    寄存器基类，定义了寄存器的基本属性
    """
    address: Union[int, Tuple[int, int]]
    """
    寄存器地址，可以是单个地址或地址范围
    
    - 单个地址: int，如 1000
    - 地址范围: Tuple[int, int]，如 (1000, 1001)
    """
