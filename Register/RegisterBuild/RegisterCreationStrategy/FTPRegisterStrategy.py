"""
FTP寄存器创建策略模块，用于从配置模块加载FTP寄存器配置
"""
import sys
import os
import logging
from typing import Dict

# 添加项目根目录到Python路径
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)

# 配置日志
logger = logging.getLogger('RH56DFTP')

# 本地导入
from Register.RegisterSet.RegisterBase import RegisterBase
from Register.RegisterSet.Register_FTP import Register_FTP
from Register.RegisterBuild.RegisterCreationStrategy.RegisterCreationStrategy import (
    RegisterCreationStrategy
)

# 配置模块导入
try:
    from Register.config.configFTP import ftp_registers
except ImportError:
    ftp_registers = None

class FTPRegisterStrategy(RegisterCreationStrategy):
    """
    FTP寄存器创建策略类，用于从配置模块加载FTP寄存器配置
    """

    def create_registers(self, config_folder_path: str = None) -> Dict[str, RegisterBase]:
        """
        从配置模块加载FTP寄存器配置并创建Register_FTP对象
        
        Args:
            config_folder_path: 配置文件夹路径（已弃用，保留用于向后兼容）
            
        Returns:
            寄存器对象字典
        """
        registers = {}

        if ftp_registers is None:
            raise ValueError("Failed to import config module: Register.config.configFTP")

        try:
            # 获取配置数据
            config_data = getattr(ftp_registers, 'REGISTERS_CONFIG', {})

            # 创建寄存器对象
            for reg_name, reg_config in config_data.items():
                register = Register_FTP(
                    name=reg_name,
                    address=reg_config['address'],
                    value_range=reg_config['value_range'],
                    range_type=reg_config['range_type'],
                    description=reg_config['description'],
                    data_type=reg_config['data_type'],
                    access_type=reg_config['access_type'],
                    default_value=reg_config.get('default_value'),
                    is_persistent=reg_config.get('is_persistent', False)
                )
                registers[reg_name] = register

            return registers
        except AttributeError as e:
            raise ValueError(f"Config module missing REGISTERS_CONFIG: {str(e)}") from e
        except Exception as e:
            raise ValueError(f"Failed to load registers from config: {str(e)}") from e

    def validate_config(self, config_data: Dict) -> bool:
        """
        验证寄存器配置数据的有效性
        
        Args:
            config_data: 寄存器配置数据
            
        Returns:
            配置数据是否有效
        """
        required_fields = ['address', 'value_range', 'range_type', 'description',
                          'data_type', 'access_type']

        for reg_name, reg_config in config_data.items():
            for field in required_fields:
                if field not in reg_config:
                    logger.error("寄存器 %s 缺少必填字段: %s", reg_name, field)
                    return False

        return True
