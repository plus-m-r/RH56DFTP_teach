import os
import sys
import re
from typing import List, Literal, Dict, Any

# 添加项目根目录到Python路径，以便能够导入config模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def build_register_keys(config_file_path: str, output_dir: str) -> None:
    """
    从配置文件中提取寄存器名称并构建Literal类型和函数库
    
    Args:
        config_file_path: 配置文件路径
        output_dir: 输出目录路径
    """
    try:
        # 从文件路径获取模块名称
        file_name = os.path.basename(config_file_path)
        module_name = file_name.replace('.py', '')
        
        # 动态导入配置文件
        import importlib.util
        spec = importlib.util.spec_from_file_location(module_name, config_file_path)
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        
        # 提取寄存器配置字典
        if hasattr(config_module, 'REGISTERS_CONFIG'):
            registers_config = config_module.REGISTERS_CONFIG
        else:
            print(f"错误: 在配置文件 {file_name} 中未找到 REGISTERS_CONFIG 变量")
            return
        
        # 提取寄存器名称
        register_names = list(registers_config.keys())
        
        # 构建Literal类型定义
        literal_definition = f"""
from typing import Literal

# 从配置文件 {file_name} 自动生成的寄存器名称Literal类型
RegisterName = Literal[{', '.join(f'\"{name}\"' for name in register_names)}]

# 所有寄存器名称列表
ALL_REGISTER_NAMES: list[RegisterName] = [{', '.join(f'\"{name}\"' for name in register_names)}]
"""
        
        # 构建函数库
        functions_library = f"""
from typing import Literal, Dict, Any

# 从配置文件 {file_name} 自动生成的寄存器函数库
RegisterName = Literal[{', '.join(f'\"{name}\"' for name in register_names)}]

# 所有寄存器名称列表
ALL_REGISTER_NAMES: list[RegisterName] = [{', '.join(f'\"{name}\"' for name in register_names)}]

"""
        
        # 为每个寄存器生成函数
        for register_name, register_info in registers_config.items():
            # 使用正则表达式替换寄存器名称中的(X)为_X，确保是有效的Python函数名
            valid_func_name = re.sub(r'\((\d+)\)', r'_\1', register_name)
            
            # 构建函数注释，包含寄存器的所有配置信息
            func_comment = f'"""\n{register_name}\n\n寄存器配置信息:\n'            
            for key, value in register_info.items():
                func_comment += f"{key}: {value}\n"
            
            func_comment += '"""'
            
            # 构建函数定义
            func_definition = f"def {valid_func_name}() -> None:\n    {func_comment}\n    pass\n\n"
            
            # 添加到函数库
            functions_library += func_definition
        
        # 构建函数名字典映射
        func_dict_entries = []
        for name in register_names:
            # 替换后的有效函数名
            valid_func_name = re.sub(r'\((\d+)\)', r'_\1', name)
            # 构建字典条目
            func_dict_entries.append(f'\"{name}": globals()[\"{valid_func_name}\"]')
        
        functions_library += f"""# 寄存器映射字典：寄存器名称 <-> 函数对象
REGISTER_MAP: Dict[RegisterName, callable] = {{
    {',\n    '.join(func_dict_entries)}
}}
"""
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 生成合并后的输出文件名
        output_file_name = f"{module_name}_keys.py"
        output_file_path = os.path.join(output_dir, output_file_name)
        
        # 写入合并后的文件（包含Literal类型定义和函数库）
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(functions_library)
        
        print(f"成功生成寄存器键文件: {output_file_path}")
        print(f"共提取 {len(register_names)} 个寄存器名称")
        
    except Exception as e:
        print(f"生成寄存器键文件时出错: {str(e)}")


def process_directory(config_dir: str, output_dir: str) -> None:
    """
    处理目录中的所有配置文件
    
    Args:
        config_dir: 配置目录路径
        output_dir: 输出目录路径
    """
    try:
        # 遍历目录中的所有.py文件
        for file_name in os.listdir(config_dir):
            if file_name.endswith('.py') and not file_name.startswith('__'):
                config_file_path = os.path.join(config_dir, file_name)
                build_register_keys(config_file_path, output_dir)
    except Exception as e:
        print(f"处理配置目录时出错: {str(e)}")


if __name__ == "__main__":
    # 默认配置目录和输出目录
    import os
    # 获取项目根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    default_config_dir = os.path.join(BASE_DIR, "Register", "config", "configFTP")
    default_output_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 处理命令行参数
    config_dir = sys.argv[1] if len(sys.argv) > 1 else default_config_dir
    output_dir = sys.argv[2] if len(sys.argv) > 2 else default_output_dir
    
    print(f"开始处理配置目录: {config_dir}")
    print(f"输出目录: {output_dir}")
    
    # 如果是目录，则处理目录中的所有文件
    if os.path.isdir(config_dir):
        process_directory(config_dir, output_dir)
    # 如果是文件，则只处理单个文件
    elif os.path.isfile(config_dir):
        build_register_keys(config_dir, output_dir)
    else:
        print(f"错误: {config_dir} 不是有效的目录或文件路径")
