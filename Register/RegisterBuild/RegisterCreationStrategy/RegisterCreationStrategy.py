import sys
import os
from typing import Dict
from abc import ABC, abstractmethod

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from Register.RegisterSet.RegisterBase import RegisterBase

# 策略抽象基类定义 - 使用配置文件夹地址作为参数
class RegisterCreationStrategy(ABC):
    @abstractmethod
    def create_registers(self, config_folder_path: str) -> Dict[str, RegisterBase]:
        """根据配置文件夹路径创建寄存器对象"""
        pass