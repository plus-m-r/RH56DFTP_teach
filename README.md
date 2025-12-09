# plusml-rh56dftp Python 库

一个用于通过 Modbus TCP 与 RH56DFTP 设备（触觉手）通信的 Python 库，由 plusml 开发。

## 功能特点

- 易于使用的 API，用于与 RH56DFTP 触觉手设备通信
- 支持读取和写入寄存器
- 内置日志系统，用于监控所有操作
- 全面的寄存器定义，包括力、电流、温度和错误数据
- 支持从所有手指和手掌获取触觉数据
- 模块化设计，便于扩展

## 安装

### 从 PyPI 安装（推荐）

您可以使用 pip 直接从 PyPI 安装该库：

```bash
pip install plusml-rh56dftp
```

### 从源代码安装

您也可以从 GitHub 仓库安装该库：

```bash
git clone https://github.com/plus-m-r/RH56DFTP_teach.git
cd RH56DFTP_teach
pip install -e .
```

### 从本地包安装

构建包后，您可以从生成的 wheel 文件安装：

```bash
pip install dist/plusml-rh56dftp-0.1.0-py3-none-any.whl
```

## 要求

- Python 3.7 或更高版本
- pymodbus 3.11.3

## 使用方法

### 基本用法

该库支持两种参数形式：函数对象和字符串形式。

```python
# 首先安装库：pip install plusml-rh56dftp
from RH56DFTP.RH56DFTP_TCP import RH56DFTP_TCP
from Register.RegisterKey.ftp_registers_keys import *

# 初始化与触觉手的连接
try:
    # 替换为您设备的 IP 地址和端口
    client = RH56DFTP_TCP(host="192.168.123.210", port=6000)
    print("✅ 成功连接到触觉手")
    
    # 1. 使用函数对象形式访问寄存器（推荐，支持 IDE 自动补全）
    print("\n1. 使用函数对象形式：")
    hand_id = client.get(HAND_ID)
    print(f"🤖 设备 ID: {hand_id}")
    
    # 使用函数对象写入寄存器
    success = client.set(HAND_ID, 2)
    print(f"🔧 设置 HAND_ID 为 2: {success}")
    
    # 读取手指力值 - 使用函数对象
    print("\n💪 力值 (g):")
    print(f"   - 小指: {client.get(FORCE_ACT_0)} g")
    print(f"   - 无名指: {client.get(FORCE_ACT_1)} g")
    print(f"   - 中指: {client.get(FORCE_ACT_2)} g")
    print(f"   - 食指: {client.get(FORCE_ACT_3)} g")
    print(f"   - 拇指弯曲: {client.get(FORCE_ACT_4)} g")
    print(f"   - 拇指旋转: {client.get(FORCE_ACT_5)} g")
    
    # 2. 使用字符串形式访问寄存器（兼容旧版本）
    print("\n2. 使用字符串形式：")
    hand_id_str = client.get("HAND_ID")
    print(f"🤖 设备 ID (字符串形式): {hand_id_str}")
    
    # 使用字符串形式读取力值
    force_0_str = client.get("FORCE_ACT(0)")
    temp_1_str = client.get("TEMP(1)")
    print(f"💪 小指力值 (字符串形式): {force_0_str} g")
    print(f"🌡️ 执行器 1 温度 (字符串形式): {temp_1_str} °C")
    
    # 关闭连接
    client.close()
    print("\n👋 连接已关闭")
except Exception as e:
    print(f"❌ 错误: {e}")
```

### 函数对象自动补全

该库支持 IDE 自动补全寄存器函数。当您输入 `client.get(` 时，您的 IDE 会显示所有可用的寄存器函数及其文档。

#### 主要优势
- **IDE 自动补全**：无需记忆寄存器名称
- **类型安全**：寄存器函数具有正确的类型
- **文档提示**：每个函数都显示寄存器详细信息
- **代码可读性**：比字符串字面量更直观

#### 可用的寄存器函数

该库为所有 71 个寄存器提供了函数，包括：
- `HAND_ID()` - 设备 ID
- `TEMP_0()`, `TEMP_1()`, ... - 执行器温度
- `FORCE_ACT_0()`, `FORCE_ACT_1()`, ... - 手指力值
- `CURRENT_0()`, `CURRENT_1()`, ... - 执行器电流值
- `POS_SET_0()`, `POS_SET_1()`, ... - 位置设置
- `ANGLE_SET_0()`, `ANGLE_SET_1()`, ... - 角度设置
- 以及更多...

### 字符串形式访问

字符串形式访问仍受支持，以保持向后兼容：

```python
# 字符串形式访问（仍受支持）
hand_id = client.get("HAND_ID")
force_0 = client.get("FORCE_ACT(0)")
temp_1 = client.get("TEMP(1)")
```

### 寄存器分类

该库提供了按功能组织的预定义寄存器名称：

#### 设备配置
- `HAND_ID`: 设备 ID (1-254)
- `REDU_RATIO`: 波特率设置
- `CLEAR_ERROR`: 清除错误命令
- `SAVE`: 将配置保存到闪存
- `RESET_PARA`: 恢复出厂设置

#### 手指力数据（只读）
- `FORCE_ACT(0)`: 小指力
- `FORCE_ACT(1)`: 无名指力  
- `FORCE_ACT(2)`: 中指力
- `FORCE_ACT(3)`: 食指力
- `FORCE_ACT(4)`: 拇指弯曲力
- `FORCE_ACT(5)`: 拇指旋转力

#### 执行器数据（只读）
- `CURRENT(0-5)`: 执行器电流值 (mA)
- `ERROR(0-5)`: 执行器错误代码
- `TEMP(0-5)`: 执行器温度值 (°C)

#### 触觉数据（只读）
- 用于所有手指和手掌的各种触觉数据寄存器
- 3x3、12x8 和 10x8 矩阵配置
- 16 位整数值 (0-4096)

## 寄存器配置

寄存器定义位于 `Register/config/configFTP` 目录中：
- `ftp_registers.py`: 主寄存器配置
- `ftp_registers_keys.py`: 寄存器名称常量

该库在初始化时会自动加载这些配置。

## 日志记录

该库包含一个内置的日志系统，用于记录：
- 所有带时间戳的 `get` 和 `set` 操作
- 连接状态和错误
- 寄存器地址和值

日志保存到 `rh56dftp.log` 文件中，并以以下格式打印到控制台：
```
YYYY-MM-DD HH:MM:SS - RH56DFTP - 级别 - 消息
```

## 项目结构

```
RH56DFTP_teach/
├── RH56DFTP/              # 主库代码
│   ├── RH56DFTP_base.py   # 抽象基类
│   ├── RH56DFTP_base.pyi  # 基类的类型提示
│   ├── RH56DFTP_TCP.py    # TCP 实现
│   ├── RH56DFTP_TCP.pyi   # TCP 实现的类型提示
│   └── __init__.py        # 包初始化
├── Register/              # 寄存器配置
│   ├── config/            # 配置文件
│   │   └── configFTP/     # FTP 寄存器配置
│   ├── RegisterKey/       # 寄存器名称常量
│   └── RegisterSet/       # 寄存器类
├── connect.py             # 示例连接脚本
├── LICENSE                # MIT 许可证文件
├── README.md              # 本文档
├── pyproject.toml         # 现代包配置
├── setup.py               # 包设置（旧版）
└── requirements.txt       # 依赖项
```

## 开发

### 构建包

要构建用于分发的包（推荐方法）：

```bash
python -m build
```

这将生成：
- `dist/plusml-rh56dftp-0.1.0.tar.gz`（源分发）
- `dist/plusml-rh56dftp-0.1.0-py3-none-any.whl`（wheel 分发）

## 许可证

MIT 许可证

## 仓库

[https://github.com/plus-m-r/RH56DFTP_teach](https://github.com/plus-m-r/RH56DFTP_teach)
