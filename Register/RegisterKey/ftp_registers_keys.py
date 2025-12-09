
from typing import Literal, Dict, Any

# 从配置文件 ftp_registers.py 自动生成的寄存器函数库
RegisterName = Literal["HAND_ID", "REDU_RATIO", "CLEAR_ERROR", "SAVE", "RESET_PARA", "GESTURE_FORCE_CALIB", "DEFAULT_SPEED_SET(0)", "DEFAULT_SPEED_SET(1)", "DEFAULT_SPEED_SET(2)", "DEFAULT_SPEED_SET(3)", "DEFAULT_SPEED_SET(4)", "DEFAULT_SPEED_SET(5)", "DEFAULT_FORCE_SET(0)", "DEFAULT_FORCE_SET(1)", "DEFAULT_FORCE_SET(2)", "DEFAULT_FORCE_SET(3)", "DEFAULT_FORCE_SET(4)", "DEFAULT_FORCE_SET(5)", "POS_SET(0)", "POS_SET(1)", "POS_SET(2)", "POS_SET(3)", "POS_SET(4)", "POS_SET(5)", "ANGLE_SET(0)", "ANGLE_SET(1)", "ANGLE_SET(2)", "ANGLE_SET(3)", "ANGLE_SET(4)", "ANGLE_SET(5)", "FORCE_ACT(0)", "FORCE_ACT(1)", "FORCE_ACT(2)", "FORCE_ACT(3)", "FORCE_ACT(4)", "FORCE_ACT(5)", "CURRENT(0)", "CURRENT(1)", "CURRENT(2)", "CURRENT(3)", "CURRENT(4)", "CURRENT(5)", "ERROR(0)", "ERROR(1)", "ERROR(2)", "ERROR(3)", "ERROR(4)", "ERROR(5)", "TEMP(0)", "TEMP(1)", "TEMP(2)", "TEMP(3)", "TEMP(4)", "TEMP(5)", "TACTILE_SMALL_FINGER_TIP_3x3", "TACTILE_SMALL_FINGER_TIP_12x8", "TACTILE_SMALL_FINGER_PALM_10x8", "TACTILE_RING_FINGER_TIP_3x3", "TACTILE_RING_FINGER_TIP_12x8", "TACTILE_RING_FINGER_PALM_10x8", "TACTILE_MIDDLE_FINGER_TIP_3x3", "TACTILE_MIDDLE_FINGER_TIP_12x8", "TACTILE_MIDDLE_FINGER_PALM_10x8", "TACTILE_INDEX_FINGER_TIP_3x3", "TACTILE_INDEX_FINGER_TIP_12x8", "TACTILE_INDEX_FINGER_PALM_10x8", "TACTILE_THUMB_TIP_3x3", "TACTILE_THUMB_TIP_12x8", "TACTILE_THUMB_MIDDLE_3x3", "TACTILE_THUMB_PALM_12x8", "TACTILE_PALM_8x14"]

# 所有寄存器名称列表
ALL_REGISTER_NAMES: list[RegisterName] = ["HAND_ID", "REDU_RATIO", "CLEAR_ERROR", "SAVE", "RESET_PARA", "GESTURE_FORCE_CALIB", "DEFAULT_SPEED_SET(0)", "DEFAULT_SPEED_SET(1)", "DEFAULT_SPEED_SET(2)", "DEFAULT_SPEED_SET(3)", "DEFAULT_SPEED_SET(4)", "DEFAULT_SPEED_SET(5)", "DEFAULT_FORCE_SET(0)", "DEFAULT_FORCE_SET(1)", "DEFAULT_FORCE_SET(2)", "DEFAULT_FORCE_SET(3)", "DEFAULT_FORCE_SET(4)", "DEFAULT_FORCE_SET(5)", "POS_SET(0)", "POS_SET(1)", "POS_SET(2)", "POS_SET(3)", "POS_SET(4)", "POS_SET(5)", "ANGLE_SET(0)", "ANGLE_SET(1)", "ANGLE_SET(2)", "ANGLE_SET(3)", "ANGLE_SET(4)", "ANGLE_SET(5)", "FORCE_ACT(0)", "FORCE_ACT(1)", "FORCE_ACT(2)", "FORCE_ACT(3)", "FORCE_ACT(4)", "FORCE_ACT(5)", "CURRENT(0)", "CURRENT(1)", "CURRENT(2)", "CURRENT(3)", "CURRENT(4)", "CURRENT(5)", "ERROR(0)", "ERROR(1)", "ERROR(2)", "ERROR(3)", "ERROR(4)", "ERROR(5)", "TEMP(0)", "TEMP(1)", "TEMP(2)", "TEMP(3)", "TEMP(4)", "TEMP(5)", "TACTILE_SMALL_FINGER_TIP_3x3", "TACTILE_SMALL_FINGER_TIP_12x8", "TACTILE_SMALL_FINGER_PALM_10x8", "TACTILE_RING_FINGER_TIP_3x3", "TACTILE_RING_FINGER_TIP_12x8", "TACTILE_RING_FINGER_PALM_10x8", "TACTILE_MIDDLE_FINGER_TIP_3x3", "TACTILE_MIDDLE_FINGER_TIP_12x8", "TACTILE_MIDDLE_FINGER_PALM_10x8", "TACTILE_INDEX_FINGER_TIP_3x3", "TACTILE_INDEX_FINGER_TIP_12x8", "TACTILE_INDEX_FINGER_PALM_10x8", "TACTILE_THUMB_TIP_3x3", "TACTILE_THUMB_TIP_12x8", "TACTILE_THUMB_MIDDLE_3x3", "TACTILE_THUMB_PALM_12x8", "TACTILE_PALM_8x14"]

# pylint: disable=invalid-name
def HAND_ID() -> None:
    """
HAND_ID

寄存器配置信息:
address: 1000
value_range: [1, 254]
range_type: continuous
description: 灵巧手ID号
data_type: uint8
access_type: read-write
default_value: 1
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def REDU_RATIO() -> None:
    """
REDU_RATIO

寄存器配置信息:
address: 1002
value_range: [0, 3]
range_type: discrete
description: 波特率设置 - RS485接口(0-3): 0=115200,1=57600,2=19200,3=921600; CAN接口(0-1): 0=1000K,1=500K
data_type: uint8
access_type: read-write
default_value: 0
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def CLEAR_ERROR() -> None:
    """
CLEAR_ERROR

寄存器配置信息:
address: 1004
value_range: [0, 1]
range_type: discrete
description: 清除错误 - 写入1后清除可清除的故障(堵转故障、过流故障、异常故障、通讯故障)，过温故障不可清除
data_type: uint8
access_type: read-write
default_value: 0
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def SAVE() -> None:
    """
SAVE

寄存器配置信息:
address: 1005
value_range: [0, 1]
range_type: discrete
description: 保存数据至Flash - 写入1后，灵巧手将当前参数写入flash，断电后参数不丢失
data_type: uint8
access_type: read-write
default_value: 0
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def RESET_PARA() -> None:
    """
RESET_PARA

寄存器配置信息:
address: 1006
value_range: [0, 1]
range_type: discrete
description: 恢复出厂设置 - 写入1后，灵巧手的参数将恢复为出厂设置参数
data_type: uint8
access_type: read-write
default_value: 0
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def GESTURE_FORCE_CALIB() -> None:
    """
GESTURE_FORCE_CALIB

寄存器配置信息:
address: 1009
value_range: [0, 1]
range_type: discrete
description: 受力传感器校准 - 设置为1时启动校准过程，必须保证灵巧手处于手掌张开状态，手指不能接触任何物体
data_type: uint8
access_type: read-write
default_value: 0
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_0() -> None:
    """
DEFAULT_SPEED_SET(0)

寄存器配置信息:
address: (1032, 1033)
value_range: [0, 1000]
range_type: continuous
description: 小拇指上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_1() -> None:
    """
DEFAULT_SPEED_SET(1)

寄存器配置信息:
address: (1034, 1035)
value_range: [0, 1000]
range_type: continuous
description: 无名指上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_2() -> None:
    """
DEFAULT_SPEED_SET(2)

寄存器配置信息:
address: (1036, 1037)
value_range: [0, 1000]
range_type: continuous
description: 中指上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_3() -> None:
    """
DEFAULT_SPEED_SET(3)

寄存器配置信息:
address: (1038, 1039)
value_range: [0, 1000]
range_type: continuous
description: 食指上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_4() -> None:
    """
DEFAULT_SPEED_SET(4)

寄存器配置信息:
address: (1040, 1041)
value_range: [0, 1000]
range_type: continuous
description: 大拇指弯曲上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_SPEED_SET_5() -> None:
    """
DEFAULT_SPEED_SET(5)

寄存器配置信息:
address: (1042, 1043)
value_range: [0, 1000]
range_type: continuous
description: 大拇指旋转上电初始速度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_0() -> None:
    """
DEFAULT_FORCE_SET(0)

寄存器配置信息:
address: (1044, 1045)
value_range: [0, 1000]
range_type: continuous
description: 小拇指上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_1() -> None:
    """
DEFAULT_FORCE_SET(1)

寄存器配置信息:
address: (1046, 1047)
value_range: [0, 1000]
range_type: continuous
description: 无名指上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_2() -> None:
    """
DEFAULT_FORCE_SET(2)

寄存器配置信息:
address: (1048, 1049)
value_range: [0, 1000]
range_type: continuous
description: 中指上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_3() -> None:
    """
DEFAULT_FORCE_SET(3)

寄存器配置信息:
address: (1050, 1051)
value_range: [0, 1000]
range_type: continuous
description: 食指上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_4() -> None:
    """
DEFAULT_FORCE_SET(4)

寄存器配置信息:
address: (1052, 1053)
value_range: [0, 1000]
range_type: continuous
description: 大拇指弯曲上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def DEFAULT_FORCE_SET_5() -> None:
    """
DEFAULT_FORCE_SET(5)

寄存器配置信息:
address: (1054, 1055)
value_range: [0, 1000]
range_type: continuous
description: 大拇指旋转上电力控阈值设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_0() -> None:
    """
POS_SET(0)

寄存器配置信息:
address: (1474, 1475)
value_range: [0, 1000]
range_type: continuous
description: 小拇指执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_1() -> None:
    """
POS_SET(1)

寄存器配置信息:
address: (1476, 1477)
value_range: [0, 1000]
range_type: continuous
description: 无名指执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_2() -> None:
    """
POS_SET(2)

寄存器配置信息:
address: (1478, 1479)
value_range: [0, 1000]
range_type: continuous
description: 中指执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_3() -> None:
    """
POS_SET(3)

寄存器配置信息:
address: (1480, 1481)
value_range: [0, 1000]
range_type: continuous
description: 食指执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_4() -> None:
    """
POS_SET(4)

寄存器配置信息:
address: (1482, 1483)
value_range: [0, 1000]
range_type: continuous
description: 大拇指弯曲执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def POS_SET_5() -> None:
    """
POS_SET(5)

寄存器配置信息:
address: (1484, 1485)
value_range: [0, 1000]
range_type: continuous
description: 大拇指旋转执行器位置设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_0() -> None:
    """
ANGLE_SET(0)

寄存器配置信息:
address: (1464, 1465)
value_range: [0, 1000]
range_type: continuous
description: 小拇指近节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_1() -> None:
    """
ANGLE_SET(1)

寄存器配置信息:
address: (1466, 1467)
value_range: [0, 1000]
range_type: continuous
description: 小拇指远节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_2() -> None:
    """
ANGLE_SET(2)

寄存器配置信息:
address: (1468, 1469)
value_range: [0, 1000]
range_type: continuous
description: 无名指近节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_3() -> None:
    """
ANGLE_SET(3)

寄存器配置信息:
address: (1470, 1471)
value_range: [0, 1000]
range_type: continuous
description: 无名指远节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_4() -> None:
    """
ANGLE_SET(4)

寄存器配置信息:
address: (1472, 1473)
value_range: [0, 1000]
range_type: continuous
description: 中指近节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def ANGLE_SET_5() -> None:
    """
ANGLE_SET(5)

寄存器配置信息:
address: (1486, 1487)
value_range: [0, 1000]
range_type: continuous
description: 中指远节指骨角度设置
data_type: short
access_type: read-write
default_value: None
is_persistent: True
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_0() -> None:
    """
FORCE_ACT(0)

寄存器配置信息:
address: (1582, 1583)
value_range: [-4000, 4000]
range_type: continuous
description: 小拇指实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_1() -> None:
    """
FORCE_ACT(1)

寄存器配置信息:
address: (1584, 1585)
value_range: [-4000, 4000]
range_type: continuous
description: 无名指实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_2() -> None:
    """
FORCE_ACT(2)

寄存器配置信息:
address: (1586, 1587)
value_range: [-4000, 4000]
range_type: continuous
description: 中指实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_3() -> None:
    """
FORCE_ACT(3)

寄存器配置信息:
address: (1588, 1589)
value_range: [-4000, 4000]
range_type: continuous
description: 食指实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_4() -> None:
    """
FORCE_ACT(4)

寄存器配置信息:
address: (1590, 1591)
value_range: [-4000, 4000]
range_type: continuous
description: 大拇指弯曲实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def FORCE_ACT_5() -> None:
    """
FORCE_ACT(5)

寄存器配置信息:
address: (1592, 1593)
value_range: [-4000, 4000]
range_type: continuous
description: 大拇指旋转实际受力值，单位：g
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_0() -> None:
    """
CURRENT(0)

寄存器配置信息:
address: (1594, 1595)
value_range: [0, 2000]
range_type: continuous
description: 小拇指执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_1() -> None:
    """
CURRENT(1)

寄存器配置信息:
address: (1596, 1597)
value_range: [0, 2000]
range_type: continuous
description: 无名指执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_2() -> None:
    """
CURRENT(2)

寄存器配置信息:
address: (1598, 1599)
value_range: [0, 2000]
range_type: continuous
description: 中指执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_3() -> None:
    """
CURRENT(3)

寄存器配置信息:
address: (1600, 1601)
value_range: [0, 2000]
range_type: continuous
description: 食指执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_4() -> None:
    """
CURRENT(4)

寄存器配置信息:
address: (1602, 1603)
value_range: [0, 2000]
range_type: continuous
description: 大拇指弯曲执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def CURRENT_5() -> None:
    """
CURRENT(5)

寄存器配置信息:
address: (1604, 1605)
value_range: [0, 2000]
range_type: continuous
description: 大拇指旋转执行器电流值，单位：mA
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_0() -> None:
    """
ERROR(0)

寄存器配置信息:
address: 1606
value_range: [0, 255]
range_type: continuous
description: 小拇指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_1() -> None:
    """
ERROR(1)

寄存器配置信息:
address: 1607
value_range: [0, 255]
range_type: continuous
description: 无名指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_2() -> None:
    """
ERROR(2)

寄存器配置信息:
address: 1608
value_range: [0, 255]
range_type: continuous
description: 中指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_3() -> None:
    """
ERROR(3)

寄存器配置信息:
address: 1609
value_range: [0, 255]
range_type: continuous
description: 食指执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_4() -> None:
    """
ERROR(4)

寄存器配置信息:
address: 1610
value_range: [0, 255]
range_type: continuous
description: 大拇指弯曲执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def ERROR_5() -> None:
    """
ERROR(5)

寄存器配置信息:
address: 1611
value_range: [0, 255]
range_type: continuous
description: 大拇指旋转执行器故障码 - Bit0:堵转故障, Bit1:过温故障, Bit2:过流故障, Bit3:电机异常, Bit4:通讯故障
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_0() -> None:
    """
TEMP(0)

寄存器配置信息:
address: 1618
value_range: [0, 100]
range_type: continuous
description: 小拇指执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_1() -> None:
    """
TEMP(1)

寄存器配置信息:
address: 1619
value_range: [0, 100]
range_type: continuous
description: 无名指执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_2() -> None:
    """
TEMP(2)

寄存器配置信息:
address: 1620
value_range: [0, 100]
range_type: continuous
description: 中指执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_3() -> None:
    """
TEMP(3)

寄存器配置信息:
address: 1621
value_range: [0, 100]
range_type: continuous
description: 食指执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_4() -> None:
    """
TEMP(4)

寄存器配置信息:
address: 1622
value_range: [0, 100]
range_type: continuous
description: 大拇指弯曲执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TEMP_5() -> None:
    """
TEMP(5)

寄存器配置信息:
address: 1623
value_range: [0, 100]
range_type: continuous
description: 大拇指旋转执行器温度值，单位：℃
data_type: uint8
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_SMALL_FINGER_TIP_3x3() -> None:
    """
TACTILE_SMALL_FINGER_TIP_3x3

寄存器配置信息:
address: (3000, 3017)
value_range: [0, 4096]
range_type: continuous
description: 小拇指指端触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_SMALL_FINGER_TIP_12x8() -> None:
    """
TACTILE_SMALL_FINGER_TIP_12x8

寄存器配置信息:
address: (3018, 3209)
value_range: [0, 4096]
range_type: continuous
description: 小拇指指尖触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_SMALL_FINGER_PALM_10x8() -> None:
    """
TACTILE_SMALL_FINGER_PALM_10x8

寄存器配置信息:
address: (3210, 3369)
value_range: [0, 4096]
range_type: continuous
description: 小拇指指腹触觉数据，10*8行列，160byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_RING_FINGER_TIP_3x3() -> None:
    """
TACTILE_RING_FINGER_TIP_3x3

寄存器配置信息:
address: (3370, 3387)
value_range: [0, 4096]
range_type: continuous
description: 无名指指端触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_RING_FINGER_TIP_12x8() -> None:
    """
TACTILE_RING_FINGER_TIP_12x8

寄存器配置信息:
address: (3388, 3579)
value_range: [0, 4096]
range_type: continuous
description: 无名指指尖触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_RING_FINGER_PALM_10x8() -> None:
    """
TACTILE_RING_FINGER_PALM_10x8

寄存器配置信息:
address: (3580, 3739)
value_range: [0, 4096]
range_type: continuous
description: 无名指指腹触觉数据，10*8行列，160byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_MIDDLE_FINGER_TIP_3x3() -> None:
    """
TACTILE_MIDDLE_FINGER_TIP_3x3

寄存器配置信息:
address: (3740, 3757)
value_range: [0, 4096]
range_type: continuous
description: 中指指端触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_MIDDLE_FINGER_TIP_12x8() -> None:
    """
TACTILE_MIDDLE_FINGER_TIP_12x8

寄存器配置信息:
address: (3758, 3949)
value_range: [0, 4096]
range_type: continuous
description: 中指指尖触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_MIDDLE_FINGER_PALM_10x8() -> None:
    """
TACTILE_MIDDLE_FINGER_PALM_10x8

寄存器配置信息:
address: (3950, 4109)
value_range: [0, 4096]
range_type: continuous
description: 中指指腹触觉数据，10*8行列，160byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_INDEX_FINGER_TIP_3x3() -> None:
    """
TACTILE_INDEX_FINGER_TIP_3x3

寄存器配置信息:
address: (4110, 4127)
value_range: [0, 4096]
range_type: continuous
description: 食指指端触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_INDEX_FINGER_TIP_12x8() -> None:
    """
TACTILE_INDEX_FINGER_TIP_12x8

寄存器配置信息:
address: (4128, 4319)
value_range: [0, 4096]
range_type: continuous
description: 食指指尖触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_INDEX_FINGER_PALM_10x8() -> None:
    """
TACTILE_INDEX_FINGER_PALM_10x8

寄存器配置信息:
address: (4320, 4479)
value_range: [0, 4096]
range_type: continuous
description: 食指指腹触觉数据，10*8行列，160byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_THUMB_TIP_3x3() -> None:
    """
TACTILE_THUMB_TIP_3x3

寄存器配置信息:
address: (4480, 4497)
value_range: [0, 4096]
range_type: continuous
description: 大拇指指端触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_THUMB_TIP_12x8() -> None:
    """
TACTILE_THUMB_TIP_12x8

寄存器配置信息:
address: (4498, 4689)
value_range: [0, 4096]
range_type: continuous
description: 大拇指指尖触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_THUMB_MIDDLE_3x3() -> None:
    """
TACTILE_THUMB_MIDDLE_3x3

寄存器配置信息:
address: (4690, 4707)
value_range: [0, 4096]
range_type: continuous
description: 大拇指中指触觉数据，3*3行列，18byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_THUMB_PALM_12x8() -> None:
    """
TACTILE_THUMB_PALM_12x8

寄存器配置信息:
address: (4708, 4899)
value_range: [0, 4096]
range_type: continuous
description: 大拇指指腹触觉数据，12*8行列，192byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# pylint: disable=invalid-name
def TACTILE_PALM_8x14() -> None:
    """
TACTILE_PALM_8x14

寄存器配置信息:
address: (4900, 5123)
value_range: [0, 4096]
range_type: continuous
description: 手掌触觉数据，8*14行列，224byte，16位整型，小端模式
data_type: short
access_type: read-only
default_value: None
is_persistent: False
"""
    pass

# 寄存器映射字典：寄存器名称 <-> 函数对象
REGISTER_MAP: Dict[RegisterName, callable] = {
    "HAND_ID": globals()["HAND_ID"],
    "REDU_RATIO": globals()["REDU_RATIO"],
    "CLEAR_ERROR": globals()["CLEAR_ERROR"],
    "SAVE": globals()["SAVE"],
    "RESET_PARA": globals()["RESET_PARA"],
    "GESTURE_FORCE_CALIB": globals()["GESTURE_FORCE_CALIB"],
    "DEFAULT_SPEED_SET(0)": globals()["DEFAULT_SPEED_SET_0"],
    "DEFAULT_SPEED_SET(1)": globals()["DEFAULT_SPEED_SET_1"],
    "DEFAULT_SPEED_SET(2)": globals()["DEFAULT_SPEED_SET_2"],
    "DEFAULT_SPEED_SET(3)": globals()["DEFAULT_SPEED_SET_3"],
    "DEFAULT_SPEED_SET(4)": globals()["DEFAULT_SPEED_SET_4"],
    "DEFAULT_SPEED_SET(5)": globals()["DEFAULT_SPEED_SET_5"],
    "DEFAULT_FORCE_SET(0)": globals()["DEFAULT_FORCE_SET_0"],
    "DEFAULT_FORCE_SET(1)": globals()["DEFAULT_FORCE_SET_1"],
    "DEFAULT_FORCE_SET(2)": globals()["DEFAULT_FORCE_SET_2"],
    "DEFAULT_FORCE_SET(3)": globals()["DEFAULT_FORCE_SET_3"],
    "DEFAULT_FORCE_SET(4)": globals()["DEFAULT_FORCE_SET_4"],
    "DEFAULT_FORCE_SET(5)": globals()["DEFAULT_FORCE_SET_5"],
    "POS_SET(0)": globals()["POS_SET_0"],
    "POS_SET(1)": globals()["POS_SET_1"],
    "POS_SET(2)": globals()["POS_SET_2"],
    "POS_SET(3)": globals()["POS_SET_3"],
    "POS_SET(4)": globals()["POS_SET_4"],
    "POS_SET(5)": globals()["POS_SET_5"],
    "ANGLE_SET(0)": globals()["ANGLE_SET_0"],
    "ANGLE_SET(1)": globals()["ANGLE_SET_1"],
    "ANGLE_SET(2)": globals()["ANGLE_SET_2"],
    "ANGLE_SET(3)": globals()["ANGLE_SET_3"],
    "ANGLE_SET(4)": globals()["ANGLE_SET_4"],
    "ANGLE_SET(5)": globals()["ANGLE_SET_5"],
    "FORCE_ACT(0)": globals()["FORCE_ACT_0"],
    "FORCE_ACT(1)": globals()["FORCE_ACT_1"],
    "FORCE_ACT(2)": globals()["FORCE_ACT_2"],
    "FORCE_ACT(3)": globals()["FORCE_ACT_3"],
    "FORCE_ACT(4)": globals()["FORCE_ACT_4"],
    "FORCE_ACT(5)": globals()["FORCE_ACT_5"],
    "CURRENT(0)": globals()["CURRENT_0"],
    "CURRENT(1)": globals()["CURRENT_1"],
    "CURRENT(2)": globals()["CURRENT_2"],
    "CURRENT(3)": globals()["CURRENT_3"],
    "CURRENT(4)": globals()["CURRENT_4"],
    "CURRENT(5)": globals()["CURRENT_5"],
    "ERROR(0)": globals()["ERROR_0"],
    "ERROR(1)": globals()["ERROR_1"],
    "ERROR(2)": globals()["ERROR_2"],
    "ERROR(3)": globals()["ERROR_3"],
    "ERROR(4)": globals()["ERROR_4"],
    "ERROR(5)": globals()["ERROR_5"],
    "TEMP(0)": globals()["TEMP_0"],
    "TEMP(1)": globals()["TEMP_1"],
    "TEMP(2)": globals()["TEMP_2"],
    "TEMP(3)": globals()["TEMP_3"],
    "TEMP(4)": globals()["TEMP_4"],
    "TEMP(5)": globals()["TEMP_5"],
    "TACTILE_SMALL_FINGER_TIP_3x3": globals()["TACTILE_SMALL_FINGER_TIP_3x3"],
    "TACTILE_SMALL_FINGER_TIP_12x8": globals()["TACTILE_SMALL_FINGER_TIP_12x8"],
    "TACTILE_SMALL_FINGER_PALM_10x8": globals()["TACTILE_SMALL_FINGER_PALM_10x8"],
    "TACTILE_RING_FINGER_TIP_3x3": globals()["TACTILE_RING_FINGER_TIP_3x3"],
    "TACTILE_RING_FINGER_TIP_12x8": globals()["TACTILE_RING_FINGER_TIP_12x8"],
    "TACTILE_RING_FINGER_PALM_10x8": globals()["TACTILE_RING_FINGER_PALM_10x8"],
    "TACTILE_MIDDLE_FINGER_TIP_3x3": globals()["TACTILE_MIDDLE_FINGER_TIP_3x3"],
    "TACTILE_MIDDLE_FINGER_TIP_12x8": globals()["TACTILE_MIDDLE_FINGER_TIP_12x8"],
    "TACTILE_MIDDLE_FINGER_PALM_10x8": globals()["TACTILE_MIDDLE_FINGER_PALM_10x8"],
    "TACTILE_INDEX_FINGER_TIP_3x3": globals()["TACTILE_INDEX_FINGER_TIP_3x3"],
    "TACTILE_INDEX_FINGER_TIP_12x8": globals()["TACTILE_INDEX_FINGER_TIP_12x8"],
    "TACTILE_INDEX_FINGER_PALM_10x8": globals()["TACTILE_INDEX_FINGER_PALM_10x8"],
    "TACTILE_THUMB_TIP_3x3": globals()["TACTILE_THUMB_TIP_3x3"],
    "TACTILE_THUMB_TIP_12x8": globals()["TACTILE_THUMB_TIP_12x8"],
    "TACTILE_THUMB_MIDDLE_3x3": globals()["TACTILE_THUMB_MIDDLE_3x3"],
    "TACTILE_THUMB_PALM_12x8": globals()["TACTILE_THUMB_PALM_12x8"],
    "TACTILE_PALM_8x14": globals()["TACTILE_PALM_8x14"]
}
