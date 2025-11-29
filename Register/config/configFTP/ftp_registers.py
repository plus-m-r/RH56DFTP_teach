from typing import Dict, List, Literal, Any
from Register.RegisterSet.Register_FTP import RangeType

# 定义配置字典类型
RegisterConfigDict = Dict[str, Dict[str, Any]]

# 配置数据
REGISTERS_CONFIG: RegisterConfigDict = {
    "HAND_ID": {
        "address": 1000,  # 使用单个地址格式更简洁
        "value_range": [1, 254],
        "range_type": "continuous",
        "description": "灵巧手ID号",
        "data_type": "uint8",
        "access_type": "read-write",  # 根据用户手册设置为读写
        "default_value": 1,  # 默认值为1
        "is_persistent": True  # 可保存
    },
    "REDU_RATIO": {
        "address": 1002,  # 波特率设置地址
        "value_range": [0, 3],  # 范围0-3（RS485接口）
        "range_type": "discrete",  # 离散值类型
        "description": "波特率设置 - RS485接口(0-3): 0=115200,1=57600,2=19200,3=921600; CAN接口(0-1): 0=1000K,1=500K",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": 0,  # 默认值为0
        "is_persistent": True  # 可保存
    },
    "CLEAR_ERROR": {
        "address": 1004,  # 清除错误地址
        "value_range": [0, 1],  # 范围0-1
        "range_type": "discrete",  # 离散值类型
        "description": "清除错误 - 写入1后清除可清除的故障(堵转故障、过流故障、异常故障、通讯故障)，过温故障不可清除",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": 0,  # 默认值为0
        "is_persistent": False  # 不可保存
    },
    "SAVE": {
        "address": 1005,  # 保存数据至Flash地址
        "value_range": [0, 1],  # 范围0-1
        "range_type": "discrete",  # 离散值类型
        "description": "保存数据至Flash - 写入1后，灵巧手将当前参数写入flash，断电后参数不丢失",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": 0,  # 默认值为0
        "is_persistent": False  # 不可保存
    },
    "RESET_PARA": {
        "address": 1006,  # 恢复出厂设置地址
        "value_range": [0, 1],  # 范围0-1
        "range_type": "discrete",  # 离散值类型
        "description": "恢复出厂设置 - 写入1后，灵巧手的参数将恢复为出厂设置参数",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": 0,  # 默认值为0
        "is_persistent": False  # 不可保存
    },
    "GESTURE_FORCE_CALIB": {
        "address": 1009,  # 受力传感器校准地址
        "value_range": [0, 1],  # 范围0-1
        "range_type": "discrete",  # 离散值类型
        "description": "受力传感器校准 - 设置为1时启动校准过程，必须保证灵巧手处于手掌张开状态，手指不能接触任何物体",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": 0,  # 默认值为0
        "is_persistent": False  # 不可保存
    },
    # 各自由度的上电速度设置值（可保存）
    "DEFAULT_SPEED_SET(0)": {
        "address": (1032, 1033),  # 小拇指上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_SPEED_SET(1)": {
        "address": (1034, 1035),  # 无名指上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_SPEED_SET(2)": {
        "address": (1036, 1037),  # 中指上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "中指上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_SPEED_SET(3)": {
        "address": (1038, 1039),  # 食指上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "食指上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_SPEED_SET(4)": {
        "address": (1040, 1041),  # 大拇指弯曲上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_SPEED_SET(5)": {
        "address": (1042, 1043),  # 大拇指旋转上电初始速度地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转上电初始速度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    # 各自由度的上电力控阈值设置值（可保存）
    "DEFAULT_FORCE_SET(0)": {
        "address": (1044, 1045),  # 小拇指上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_FORCE_SET(1)": {
        "address": (1046, 1047),  # 无名指上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_FORCE_SET(2)": {
        "address": (1048, 1049),  # 中指上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "中指上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_FORCE_SET(3)": {
        "address": (1050, 1051),  # 食指上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "食指上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_FORCE_SET(4)": {
        "address": (1052, 1053),  # 大拇指弯曲上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "DEFAULT_FORCE_SET(5)": {
        "address": (1054, 1055),  # 大拇指旋转上电力控阈值地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转上电力控阈值设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    # 各自由度的执行器位置设置值（可保存）
    "POS_SET(0)": {
        "address": (1474, 1475),  # 小拇指执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "POS_SET(1)": {
        "address": (1476, 1477),  # 无名指执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "POS_SET(2)": {
        "address": (1478, 1479),  # 中指执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "中指执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "POS_SET(3)": {
        "address": (1480, 1481),  # 食指执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "食指执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "POS_SET(4)": {
        "address": (1482, 1483),  # 大拇指弯曲执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "POS_SET(5)": {
        "address": (1484, 1485),  # 大拇指旋转执行器位置设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转执行器位置设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    # 各自由度的角度设置值（可保存）
    "ANGLE_SET(0)": {
        "address": (1464, 1465),  # 小拇指近节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指近节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "ANGLE_SET(1)": {
        "address": (1466, 1467),  # 小拇指远节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指远节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "ANGLE_SET(2)": {
        "address": (1468, 1469),  # 无名指近节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指近节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "ANGLE_SET(3)": {
        "address": (1470, 1471),  # 无名指远节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指远节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "ANGLE_SET(4)": {
        "address": (1472, 1473),  # 中指近节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "中指近节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    "ANGLE_SET(5)": {
        "address": (1486, 1487),  # 中指远节指骨角度设置地址范围
        "value_range": [0, 1000],  # 范围0-1000
        "range_type": "continuous",  # 连续值类型
        "description": "中指远节指骨角度设置",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-write",  # 读写类型
        "default_value": None,  # 默认值未指定
        "is_persistent": True  # 可保存
    },
    # 各手指实际受力值（只读）
    "FORCE_ACT(0)": {
        "address": (1582, 1583),  # 小拇指实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "FORCE_ACT(1)": {
        "address": (1584, 1585),  # 无名指实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "FORCE_ACT(2)": {
        "address": (1586, 1587),  # 中指实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "中指实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "FORCE_ACT(3)": {
        "address": (1588, 1589),  # 食指实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "食指实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "FORCE_ACT(4)": {
        "address": (1590, 1591),  # 大拇指弯曲实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "FORCE_ACT(5)": {
        "address": (1592, 1593),  # 大拇指旋转实际受力值地址范围
        "value_range": [-4000, 4000],  # 范围-4000-4000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转实际受力值，单位：g",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 各执行器电流值（只读）
    "CURRENT(0)": {
        "address": (1594, 1595),  # 小拇指执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "CURRENT(1)": {
        "address": (1596, 1597),  # 无名指执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "无名指执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "CURRENT(2)": {
        "address": (1598, 1599),  # 中指执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "中指执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "CURRENT(3)": {
        "address": (1600, 1601),  # 食指执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "食指执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "CURRENT(4)": {
        "address": (1602, 1603),  # 大拇指弯曲执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "CURRENT(5)": {
        "address": (1604, 1605),  # 大拇指旋转执行器电流值地址范围
        "value_range": [0, 2000],  # 范围0-2000
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转执行器电流值，单位：mA",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 各执行器故障码（只读）
    "ERROR(0)": {
        "address": 1606,  # 小拇指执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "ERROR(1)": {
        "address": 1607,  # 无名指执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "无名指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "ERROR(2)": {
        "address": 1608,  # 中指执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "中指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "ERROR(3)": {
        "address": 1609,  # 食指执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "食指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "ERROR(4)": {
        "address": 1610,  # 大拇指弯曲执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "ERROR(5)": {
        "address": 1611,  # 大拇指旋转执行器故障码地址
        "value_range": [0, 255],  # 范围0-255
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 各执行器温度（只读）
    "TEMP(0)": {
        "address": 1618,  # 小拇指执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TEMP(1)": {
        "address": 1619,  # 无名指执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "无名指执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TEMP(2)": {
        "address": 1620,  # 中指执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "中指执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TEMP(3)": {
        "address": 1621,  # 食指执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "食指执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TEMP(4)": {
        "address": 1622,  # 大拇指弯曲执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指弯曲执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TEMP(5)": {
        "address": 1623,  # 大拇指旋转执行器温度值地址
        "value_range": [0, 100],  # 范围0-100
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指旋转执行器温度值，单位：℃",
        "data_type": "uint8",  # 1byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 触觉数据寄存器（只读）
    # 小拇指触觉数据
    "TACTILE_SMALL_FINGER_TIP_3x3": {
        "address": (3000, 3017),  # 小拇指指端触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指指端触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_SMALL_FINGER_TIP_12x8": {
        "address": (3018, 3209),  # 小拇指指尖触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指指尖触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_SMALL_FINGER_PALM_10x8": {
        "address": (3210, 3369),  # 小拇指指腹触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "小拇指指腹触觉数据，10*8行列，160byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 无名指触觉数据
    "TACTILE_RING_FINGER_TIP_3x3": {
        "address": (3370, 3387),  # 无名指指端触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "无名指指端触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_RING_FINGER_TIP_12x8": {
        "address": (3388, 3579),  # 无名指指尖触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "无名指指尖触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_RING_FINGER_PALM_10x8": {
        "address": (3580, 3739),  # 无名指指腹触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "无名指指腹触觉数据，10*8行列，160byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 中指触觉数据
    "TACTILE_MIDDLE_FINGER_TIP_3x3": {
        "address": (3740, 3757),  # 中指指端触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "中指指端触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_MIDDLE_FINGER_TIP_12x8": {
        "address": (3758, 3949),  # 中指指尖触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "中指指尖触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_MIDDLE_FINGER_PALM_10x8": {
        "address": (3950, 4109),  # 中指指腹触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "中指指腹触觉数据，10*8行列，160byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 食指触觉数据
    "TACTILE_INDEX_FINGER_TIP_3x3": {
        "address": (4110, 4127),  # 食指指端触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "食指指端触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_INDEX_FINGER_TIP_12x8": {
        "address": (4128, 4319),  # 食指指尖触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "食指指尖触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_INDEX_FINGER_PALM_10x8": {
        "address": (4320, 4479),  # 食指指腹触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "食指指腹触觉数据，10*8行列，160byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 大拇指触觉数据
    "TACTILE_THUMB_TIP_3x3": {
        "address": (4480, 4497),  # 大拇指指端触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指指端触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_THUMB_TIP_12x8": {
        "address": (4498, 4689),  # 大拇指指尖触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指指尖触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_THUMB_MIDDLE_3x3": {
        "address": (4690, 4707),  # 大拇指中指触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指中指触觉数据，3*3行列，18byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    "TACTILE_THUMB_PALM_12x8": {
        "address": (4708, 4899),  # 大拇指指腹触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "大拇指指腹触觉数据，12*8行列，192byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    },
    # 手掌触觉数据
    "TACTILE_PALM_8x14": {
        "address": (4900, 5123),  # 手掌触觉数据地址范围
        "value_range": [0, 4096],  # 范围0-4096
        "range_type": "continuous",  # 连续值类型
        "description": "手掌触觉数据，8*14行列，224byte，16位整型，小端模式",
        "data_type": "short",  # 2byte数据类型
        "access_type": "read-only",  # 只读类型
        "default_value": None,  # 默认值未指定
        "is_persistent": False  # 不可保存
    }
}