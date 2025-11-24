#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
网络扫描工具
用于扫描电脑所连网线连接到的所有开放IP及端口

功能说明：
1. 自动检测本机IP和子网
2. 扫描局域网内的活跃主机
3. 扫描指定主机或所有活跃主机的开放端口
4. 支持多线程扫描以提高效率
"""

import socket
import subprocess
import ipaddress
import threading
import time
import concurrent.futures
from typing import List, Dict, Set
import platform


def get_local_ip() -> str:
    """
    获取本机IP地址
    """
    try:
        # 创建一个UDP socket连接到一个公共IP，这样可以获取本机用于对外通信的IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # 连接到Google的DNS服务器
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"获取本地IP失败: {e}")
        return "127.0.0.1"


def get_subnet_ips(local_ip: str, subnet_mask: str = "24") -> List[str]:
    """
    根据本机IP获取子网内所有IP地址
    """
    try:
        # 构建CIDR格式的网络地址
        network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)
        # 返回网络中的所有IP地址，排除网络地址和广播地址
        return [str(ip) for ip in network.hosts()]
    except Exception as e:
        print(f"获取子网IP失败: {e}")
        return []


def ping_host(ip: str) -> bool:
    """
    使用ping命令检查主机是否活跃
    """
    try:
        # 根据操作系统使用不同的ping命令参数
        param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        # 执行ping命令，超时设置为1秒
        result = subprocess.run(
            ["ping", param, ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=1
        )
        # 返回命令是否成功执行
        return result.returncode == 0
    except Exception:
        return False


def scan_active_hosts(subnet_ips: List[str], max_workers: int = 100) -> List[str]:
    """
    扫描子网内的所有活跃主机
    """
    active_hosts = []
    print(f"开始扫描子网内的活跃主机，共{len(subnet_ips)}个IP地址...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有ping任务
        future_to_ip = {executor.submit(ping_host, ip): ip for ip in subnet_ips}
        # 处理完成的任务
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                if future.result():
                    active_hosts.append(ip)
                    print(f"发现活跃主机: {ip}")
            except Exception:
                pass
    
    print(f"扫描完成，共发现{len(active_hosts)}个活跃主机")
    return active_hosts


def scan_port(ip: str, port: int) -> bool:
    """
    扫描指定IP的指定端口是否开放
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # 设置超时时间为0.5秒
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0  # 返回端口是否开放
    except Exception:
        return False


def scan_ports(ip: str, ports: List[int], max_workers: int = 100) -> List[int]:
    """
    扫描指定IP的多个端口
    """
    open_ports = []
    print(f"开始扫描主机 {ip} 的端口，共{len(ports)}个端口...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有端口扫描任务
        future_to_port = {executor.submit(scan_port, ip, port): port for port in ports}
        # 处理完成的任务
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    open_ports.append(port)
                    print(f"主机 {ip}: 端口 {port} 开放")
            except Exception:
                pass
    
    return sorted(open_ports)


def main():
    """
    主函数，扫描局域网内的活跃主机和开放端口
    """
    try:
        # 获取本机IP
        local_ip = get_local_ip()
        print(f"本机IP地址: {local_ip}")
        
        # 获取子网IP列表
        subnet_ips = get_subnet_ips(local_ip)
        
        # 扫描活跃主机
        active_hosts = scan_active_hosts(subnet_ips)
        
        if not active_hosts:
            print("未发现活跃主机")
            return
        
        # 定义要扫描的端口范围
        common_ports = list(range(1, 1025))  # 常用端口
        # 也可以添加一些额外的常用端口
        additional_ports = [8080, 8443, 3306, 5432, 27017, 6379]  # Web服务器、数据库等
        ports_to_scan = common_ports + additional_ports
        
        # 扫描每个活跃主机的端口
        scan_results = {}
        for host in active_hosts:
            open_ports = scan_ports(host, ports_to_scan)
            scan_results[host] = open_ports
        
        # 打印扫描结果摘要
        print("\n=== 扫描结果摘要 ===")
        for host, ports in scan_results.items():
            if ports:
                print(f"主机 {host} 开放的端口: {', '.join(map(str, ports))}")
            else:
                print(f"主机 {host} 未发现开放端口")
        
    except KeyboardInterrupt:
        print("\n扫描被用户中断")
    except Exception as e:
        print(f"扫描过程中发生错误: {e}")


if __name__ == "__main__":
    print("======== 网络扫描工具 ========")
    print("扫描电脑所连网线连接到的所有开放IP及端口")
    print("注意: 请确保您有权限扫描这些设备，避免未授权扫描\n")
    main()
    print("\n扫描完成!")