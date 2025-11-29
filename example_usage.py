#!/usr/bin/env python3
"""
RH56DFTP 示例运行代码

这个示例展示了如何使用 plusml-rh56dftp 库连接到触觉手设备，
读取设备信息、传感器数据，并设置设备参数。
"""

import traceback
from RH56DFTP.RH56DFTP_TCP import RH56DFTPClient

def example_usage():
    """示例使用函数"""
    # 设备连接参数
    host = "192.168.123.210"
    port = 6000

    try:
        # 1. 创建客户端实例，连接到设备
        print("正在连接到触觉手设备...")
        client = RH56DFTPClient(host=host, port=port)
        print("✅ 连接成功！")

        # 2. 读取设备基本信息
        print("\n=== 设备基本信息 ===")
        hand_id = client.get("HAND_ID")
        print(f"🤖 设备ID: {hand_id}")

        # 3. 读取温度数据
        print("\n=== 执行器温度 ===")
        for i in range(6):
            temp = client.get(f"TEMP({i})")
            print(f"🌡️  执行器 {i}: {temp} °C")

        # 4. 读取力值数据
        print("\n=== 手指力值 ===")
        finger_names = ["小指", "无名指", "中指", "食指", "拇指弯曲", "拇指旋转"]
        for i, finger_name in enumerate(finger_names):
            force = client.get(f"FORCE_ACT({i})")
            print(f"✋ {finger_name}: {force} g")

        # 5. 读取电流数据
        print("\n=== 执行器电流 ===")
        for i in range(6):
            current = client.get(f"CURRENT({i})")
            print(f"⚡ 执行器 {i}: {current} mA")

        # 6. 读取错误码
        print("\n=== 执行器错误码 ===")
        for i in range(6):
            error = client.get(f"ERROR({i})")
            print(f"⚠️  执行器 {i}: 错误码={error}")

        # 7. 设置设备参数示例
        print("\n=== 设置设备参数 ===")

        # 7.1 清除错误
        print("正在清除错误...")
        result = client.set("CLEAR_ERROR", 1)
        if result:
            print("✅ 成功清除错误")
        else:
            print("❌ 清除错误失败")

        # 7.2 设置小拇指位置（示例值，实际使用时请根据设备手册调整）
        test_pos = 500
        print(f"正在设置小拇指位置为 {test_pos}...")
        result = client.set("POS_SET(0)", test_pos)
        if result:
            print(f"✅ 成功设置小拇指位置为 {test_pos}")
            # 读取验证
            read_pos = client.get("POS_SET(0)")
            print(f"🔍 验证读取: 小拇指位置 = {read_pos}")
        else:
            print("❌ 设置小拇指位置失败")

        # 8. 关闭连接
        print("\n=== 关闭连接 ===")
        client.close()
        print("👋 连接已关闭")

    except (ConnectionError, ValueError, TypeError) as e:
        print(f"❌ 发生错误: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    example_usage()
