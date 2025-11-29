from typing import Union, Literal, Tuple, Any, Optional
from dataclasses import dataclass
from .RegisterBase import RegisterBase

RangeType = Literal["discrete", "continuous"]
DataType = Literal["int8", "int16", "int32", "uint8", "uint16", "uint32", "float", "short"]
AccessType = Literal["read-only", "write-only", "read-write"]

@dataclass(frozen=True)
class Register_FTP(RegisterBase):
    """
    FTP寄存器类，继承自RegisterBase
    """
    address: Union[int, Tuple[int, int]]
    """
    寄存器地址，可以是单个地址或地址范围
    
    - 单个地址: int，如 1000
    - 地址范围: Tuple[int, int]，如 (1000, 1001)
    """
    
    value_range: Union[Tuple[Any, ...], Tuple[Union[int, float], Union[int, float]]]
    """
    寄存器值的范围
    
    - 离散值: Tuple[Any, ...]，如 (0, 1, 2)
    - 连续值: Tuple[Union[int, float], Union[int, float]]，如 (0, 1000)
    """
    
    range_type: RangeType
    """
    范围类型
    
    - "discrete": 离散值
    - "continuous": 连续值
    """
    
    description: str
    """
    寄存器描述
    """
    
    data_type: DataType
    """
    数据类型
    
    - "int8": 8位有符号整数
    - "int16": 16位有符号整数
    - "int32": 32位有符号整数
    - "uint8": 8位无符号整数
    - "uint16": 16位无符号整数
    - "uint32": 32位无符号整数
    - "float": 浮点数
    - "short": 短整数
    """
    
    access_type: AccessType
    """
    访问类型
    
    - "read-only": 只读
    - "write-only": 只写
    - "read-write": 读写
    """
    
    default_value: Optional[Any] = None
    """
    默认值
    """
    
    is_persistent: bool = False
    """
    是否持久化
    
    - True: 保存到Flash，断电不丢失
    - False: 临时值，断电丢失
    """
