import easygui
import time
import random
import os
import subprocess
import sys
from threading import Thread

# 存储所有打开的CMD进程
cmd_processes = []

def fake_cmd_window():
    """模拟CMD窗口弹出效果"""
    for _ in range(5):
        try:
            cmd = subprocess.Popen(
                ['cmd', '/k', 'echo 警告: 系统检测到异常活动! && color 0C && mode con: cols=40 lines=5 && title 系统警报 && ping 127.0.0.1 -n 3 >nul'],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
            cmd_processes.append(cmd)
            time.sleep(0.3)
        except:
            continue

def cleanup_cmd_windows():
    """关闭所有打开的CMD窗口"""
    for proc in cmd_processes:
        try:
            proc.terminate()
        except:
            pass
    os.system('taskkill /f /im cmd.exe >nul 2>&1')

def auto_progress():
    """自动滑动进度条"""
    progress = 0
    msg = "文件加密进度: 0%\n\n正在加密您的个人文件..."
    
    while progress < 100:
        try:
            # 更新进度，确保不超过100
            progress = min(progress + random.randint(5, 15), 100)
            
            # 显示滑动条
            progress = easygui.slider(
                msg,
                title="🛑 系统紧急警报 🛑",
                default=progress,
                min_value=0,
                max_value=100,
                orientation="horizontal"
            )
            
            # 如果用户关闭窗口，继续执行
            if progress is None:
                progress = 100
            
            msg = f"文件加密进度: {progress}%\n\n已加密文件: {random.randint(100, 500)}个"
            time.sleep(0.5)
            
        except Exception as e:
            print(f"发生错误: {e}")
            progress = 100

def fake_hacking():
    """模拟黑客攻击过程"""
    try:
        # 第一阶段：警告
        fake_cmd_window()
        easygui.msgbox("检测到黑客入侵!\n\n您的系统安全已被破坏...", title="🚨 紧急安全警报 🚨", ok_button="确定 (无法取消)")
        
        # 第二阶段：加密过程
        easygui.msgbox("正在扫描您的个人文件...\n\n已找到敏感数据: 照片、文档、密码", title="🔍 文件扫描中 🔍")
        auto_progress()
        
        # 第三阶段：勒索
        easygui.msgbox("您的所有文件已被加密!\n\n请在24小时内支付0.1比特币到:\n黑客钱包: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", 
                      title="💀 系统被锁定 💀")
        
        # 最终揭示玩笑
        easygui.msgbox("哈哈，骗你的啦! 😜\n\n这只是个无害的玩笑程序\n您的电脑其实很安全~", 
                      title="🎉 愚人节快乐 🎉", 
                      ok_button="呼...吓死我了")
    
    finally:
        cleanup_cmd_windows()

def main():
    try:
        # 伪装成系统更新
        choice = easygui.buttonbox("Windows Defender 紧急安全更新\n\n检测到严重系统漏洞，必须立即修复", 
                                 title="Windows 安全中心", 
                                 choices=["立即修复", "稍后提醒 (不推荐)"])
        
        # 无论用户选择什么都会执行
        fake_hacking()
        
    except KeyboardInterrupt:
        pass
    finally:
        cleanup_cmd_windows()
        sys.exit(0)

if __name__ == "__main__":
    main()