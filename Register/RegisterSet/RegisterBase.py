from typing import Tuple,Union
from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterBase:
    address: Union[int, Tuple[int, int]]