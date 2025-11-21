import sys
import os
import json
import importlib.util
from typing import Dict

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from Register.RegisterSet.RegisterBase import RegisterBase
from Register.RegisterSet.Register_FTP import Register_FTP
from Register.RegisterBuild.RegisterCreationStrategy.RegisterCreationStrategy import RegisterCreationStrategy

class FTPRegisterStrategy(RegisterCreationStrategy):
    def create_registers(self, config_folder_path: str) -> Dict[str, RegisterBase]:
        """从配置文件夹加载FTP寄存器配置并创建Register_FTP对象"""
        registers = {}
        # 遍历配置文件夹中的所有.json和.py文件
        for filename in os.listdir(config_folder_path):
            filepath = os.path.join(config_folder_path, filename)
            try:
                if filename.endswith('.json'):
                    # 处理JSON配置文件
                    with open(filepath, 'r', encoding='utf-8') as f:
                        config_data = json.load(f)
                elif filename.endswith('.py') and not filename.startswith('__'):
                    # 处理Python配置文件
                    module_name = filename[:-3]  # 移除.py后缀
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        # 假设配置数据在模块的REGISTERS_CONFIG变量中
                        config_data = getattr(module, 'REGISTERS_CONFIG', {})
                    else:
                        print(f"Failed to load module {module_name} from {filepath}")
                        continue
                else:
                    continue

                # 创建寄存器对象
                for reg_name, reg_config in config_data.items():
                    register = Register_FTP(
                        address=reg_config['address'],
                        value_range=reg_config['value_range'],
                        range_type=reg_config['range_type'],
                        description=reg_config['description'],
                        data_type=reg_config['data_type'],
                        access_type=reg_config['access_type'],
                        default_value=reg_config.get('default_value'),  # 可选字段，使用get避免KeyError
                        is_persistent=reg_config.get('is_persistent', False)  # 可选字段，默认为False
                    )
                    registers[reg_name] = register
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
        return registers