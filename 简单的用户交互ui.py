import os
import json
import time
import hashlib
from getpass import getpass
from typing import Dict, Optional

# ANSI 颜色代码
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

# 渐变色颜色列表
GRADIENT_COLORS = [
    '\033[38;5;196m',  # 红色
    '\033[38;5;202m',  # 橙红
    '\033[38;5;208m',  # 橙色
    '\033[38;5;214m',  # 橙黄
    '\033[38;5;220m',  # 黄色
    '\033[38;5;226m',  # 亮黄
    '\033[38;5;46m',   # 绿色
    '\033[38;5;48m',   # 亮绿
    '\033[38;5;51m',   # 青色
    '\033[38;5;45m',   # 亮蓝
    '\033[38;5;39m',   # 蓝色
    '\033[38;5;93m',   # 紫色
    '\033[38;5;129m',  # 紫红
]

# 文件路径
DATA_FILE = "C:/users_data.json"

def animate_gradient_text(text: str, delay: float = 0.05) -> None:
    """显示带有渐变动画效果的文本"""
    for i, char in enumerate(text):
        color = GRADIENT_COLORS[i % len(GRADIENT_COLORS)]
        print(f"{color}{char}", end='', flush=True)
        time.sleep(delay)
    print(Colors.RESET)

def clear_screen() -> None:
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title: str) -> None:
    """显示标题"""
    clear_screen()
    print("\n" + "="*50)
    animate_gradient_text(f"  {title.center(46)}  ")
    print("="*50 + "\n")

def hash_password(password: str) -> str:
    """使用SHA-256哈希密码"""
    return hashlib.sha256(password.encode()).hexdigest()

def load_users() -> Dict[str, Dict[str, str]]:
    """从文件加载用户数据"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
    except (json.JSONDecodeError, IOError):
        pass
    return {}

def save_users(users: Dict[str, Dict[str, str]]) -> None:
    """保存用户数据到文件"""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(users, file, indent=4)
    except IOError as e:
        print(f"{Colors.RED}保存数据时出错: {e}{Colors.RESET}")

def register_user() -> None:
    """用户注册"""
    display_header("用户注册")
    
    users = load_users()
    
    while True:
        username = input(f"{Colors.CYAN}请输入用户名 (至少4个字符): {Colors.RESET}").strip()
        if len(username) < 4:
            print(f"{Colors.YELLOW}用户名必须至少4个字符!{Colors.RESET}")
            continue
            
        if username in users:
            print(f"{Colors.RED}用户名已存在!{Colors.RESET}")
            time.sleep(1)
            return
            
        break
    
    while True:
        password = getpass(f"{Colors.CYAN}请输入密码 (至少6个字符): {Colors.RESET}").strip()
        if len(password) < 6:
            print(f"{Colors.YELLOW}密码必须至少6个字符!{Colors.RESET}")
            continue
            
        confirm_password = getpass(f"{Colors.CYAN}请确认密码: {Colors.RESET}").strip()
        if password != confirm_password:
            print(f"{Colors.RED}密码不匹配!{Colors.RESET}")
            continue
            
        break
    
    # 存储用户信息 (密码哈希)
    users[username] = {
        'password_hash': hash_password(password),
        'register_time': time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    save_users(users)
    
    print(f"{Colors.GREEN}\n注册成功!{Colors.RESET}")
    animate_gradient_text("欢迎加入我们的系统!")
    time.sleep(2)

def login_user() -> Optional[str]:
    """用户登录"""
    display_header("用户登录")
    
    users = load_users()
    
    username = input(f"{Colors.CYAN}请输入用户名: {Colors.RESET}").strip()
    password = getpass(f"{Colors.CYAN}请输入密码: {Colors.RESET}").strip()
    
    if username not in users:
        print(f"{Colors.RED}\n用户名不存在!{Colors.RESET}")
        time.sleep(1)
        return None
    
    if users[username]['password_hash'] != hash_password(password):
        print(f"{Colors.RED}\n密码错误!{Colors.RESET}")
        time.sleep(1)
        return None
    
    print(f"{Colors.GREEN}\n登录成功!{Colors.RESET}")
    animate_gradient_text(f"欢迎回来, {username}!")
    time.sleep(2)
    return username

def main_menu() -> None:
    """主菜单"""
    while True:
        display_header("用户管理系统")
        
        print(f"{Colors.BLUE}1. 注册{Colors.RESET}")
        print(f"{Colors.BLUE}2. 登录{Colors.RESET}")
        print(f"{Colors.BLUE}3. 退出{Colors.RESET}")
        
        choice = input(f"{Colors.CYAN}\n请选择操作 (1-3): {Colors.RESET}").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            logged_in_user = login_user()
            if logged_in_user:
                user_dashboard(logged_in_user)
        elif choice == '3':
            animate_gradient_text("感谢使用，再见!")
            time.sleep(1)
            break
        else:
            print(f"{Colors.RED}无效选择，请重新输入!{Colors.RESET}")
            time.sleep(1)

def user_dashboard(username: str) -> None:
    """用户仪表盘"""
    while True:
        display_header("用户中心")
        
        users = load_users()
        user_data = users.get(username, {})
        reg_time = user_data.get('register_time', '未知时间')
        
        print(f"{Colors.GREEN}欢迎, {username}!{Colors.RESET}")
        print(f"{Colors.YELLOW}注册时间: {reg_time}{Colors.RESET}")
        print(f"\n{Colors.BLUE}1. 查看个人信息{Colors.RESET}")
        print(f"{Colors.BLUE}2. 修改密码{Colors.RESET}")
        print(f"{Colors.BLUE}3. 注销{Colors.RESET}")
        
        choice = input(f"{Colors.CYAN}\n请选择操作 (1-3): {Colors.RESET}").strip()
        
        if choice == '1':
            display_user_info(username)
        elif choice == '2':
            change_password(username)
        elif choice == '3':
            print(f"{Colors.GREEN}\n注销成功!{Colors.RESET}")
            time.sleep(1)
            break
        else:
            print(f"{Colors.RED}无效选择，请重新输入!{Colors.RESET}")
            time.sleep(1)

def display_user_info(username: str) -> None:
    """显示用户信息"""
    display_header("个人信息")
    
    users = load_users()
    user_data = users.get(username, {})
    reg_time = user_data.get('register_time', '未知时间')
    
    print(f"{Colors.CYAN}用户名: {username}{Colors.RESET}")
    print(f"{Colors.CYAN}注册时间: {reg_time}{Colors.RESET}")
    
    input(f"{Colors.CYAN}\n按Enter键返回...{Colors.RESET}")

def change_password(username: str) -> None:
    """修改密码"""
    display_header("修改密码")
    
    users = load_users()
    
    while True:
        current_password = getpass(f"{Colors.CYAN}请输入当前密码: {Colors.RESET}").strip()
        
        if users[username]['password_hash'] != hash_password(current_password):
            print(f"{Colors.RED}\n当前密码错误!{Colors.RESET}")
            time.sleep(1)
            return
            
        new_password = getpass(f"{Colors.CYAN}请输入新密码 (至少6个字符): {Colors.RESET}").strip()
        if len(new_password) < 6:
            print(f"{Colors.YELLOW}密码必须至少6个字符!{Colors.RESET}")
            continue
            
        confirm_password = getpass(f"{Colors.CYAN}请确认新密码: {Colors.RESET}").strip()
        if new_password != confirm_password:
            print(f"{Colors.RED}密码不匹配!{Colors.RESET}")
            continue
            
        # 更新密码
        users[username]['password_hash'] = hash_password(new_password)
        save_users(users)
        
        print(f"{Colors.GREEN}\n密码修改成功!{Colors.RESET}")
        time.sleep(2)
        break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"{Colors.RED}\n程序被用户中断{Colors.RESET}")
        exit(0)
    except Exception as e:
        print(f"{Colors.RED}\n发生错误: {e}{Colors.RESET}")
        exit(1)