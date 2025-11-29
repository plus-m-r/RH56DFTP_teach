from typing import Union,Literal,Tuple,Dict,Any,Optional
from dataclasses import dataclass
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Register.RegisterSet.RegisterBase import RegisterBase

RangeType = Literal["discrete","continuous"]
DataType = Literal["int8","int16","int32","uint8","uint16","uint32","float","short"] 
AccessType = Literal["read-only","write-only","read-write"]

@dataclass(frozen=True)
class Register_FTP(RegisterBase):
    name:str
    address:Union[int, Tuple[int, int]]
    value_range:Union[Tuple[Any,...],Tuple[Union[int,float],Union[int,float]]]
    range_type:RangeType
    description:str
    data_type:DataType
    access_type:AccessType
    default_value: Optional[Any] = None 
    is_persistent: bool = False