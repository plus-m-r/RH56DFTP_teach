import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import Dict
from Register.RegisterSet.RegisterBase import RegisterBase
from Register.RegisterBuild.RegisterCreationStrategy.RegisterCreationStrategy import RegisterCreationStrategy
from Register.RegisterBuild.RegisterCreationStrategy.FTPRegisterStrategy import FTPRegisterStrategy

class RegisterFactory:
    def __init__(self):
        self._strategies: Dict[str, RegisterCreationStrategy] = {}
        # 注册默认策略
        self.register_strategy('ftp', FTPRegisterStrategy())
    
    def register_strategy(self, strategy_name: str, strategy: RegisterCreationStrategy) -> None:
        """注册新的寄存器创建策略"""
        self._strategies[strategy_name] = strategy
    
    def create_registers(self, config_folder_path: str, strategy_name: str = 'ftp') -> Dict[str, RegisterBase]:
        """使用指定策略从配置文件夹创建寄存器"""
        strategy = self._strategies.get(strategy_name)
        if not strategy:
            raise ValueError(f"Unknown strategy: {strategy_name}")
        return strategy.create_registers(config_folder_path)

# 创建全局工厂实例供外部使用
register_factory = RegisterFactory()

if __name__ == "__main__":
    registers = register_factory.create_registers(config_folder_path="Register/config/configFTP",strategy_name='ftp')
    print(registers)
