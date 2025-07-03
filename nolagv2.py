#!/usr/bin/env python3
import os
import sys
import time
import psutil
import subprocess
import threading
import signal
import platform
from datetime import datetime

def gradient_2(text):
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    # 🎨 Màu gradient nổi bật hơn
    start_color = (255, 87, 34)     # 🧡 Cam đất
    mid_color   = (255, 20, 147)    # 💖 Hồng đậm neon
    end_color   = (255, 255, 0)     # 💛 Vàng sáng

    steps = len(text)
    result = ""

    for i, char in enumerate(text):
        t = i / (steps - 1 if steps > 1 else 1)

        if t < 0.5:
            t2 = t / 0.5
            r = int(start_color[0] + (mid_color[0] - start_color[0]) * t2)
            g = int(start_color[1] + (mid_color[1] - start_color[1]) * t2)
            b = int(start_color[2] + (mid_color[2] - start_color[2]) * t2)
        else:
            t2 = (t - 0.5) / 0.5
            r = int(mid_color[0] + (end_color[0] - mid_color[0]) * t2)
            g = int(mid_color[1] + (end_color[1] - mid_color[1]) * t2)
            b = int(mid_color[2] + (end_color[2] - mid_color[2]) * t2)

        result += rgb_to_ansi(r, g, b) + char

    return result + "\033[0m"
    
def gradient_1(text):
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    # 🎨 Màu gradient nổi bật hơn
    start_color = (0, 128, 255)     # 💧 Xanh dương đậm
    mid_color   = (0, 255, 255)     # 🧊 Cyan sáng
    end_color   = (255, 255, 255)   # ⚪ Trắng sáng

    steps = len(text)
    result = ""

    for i, char in enumerate(text):
        t = i / (steps - 1 if steps > 1 else 1)

        if t < 0.5:
            t2 = t / 0.5
            r = int(start_color[0] + (mid_color[0] - start_color[0]) * t2)
            g = int(start_color[1] + (mid_color[1] - start_color[1]) * t2)
            b = int(start_color[2] + (mid_color[2] - start_color[2]) * t2)
        else:
            t2 = (t - 0.5) / 0.5
            r = int(mid_color[0] + (end_color[0] - mid_color[0]) * t2)
            g = int(mid_color[1] + (end_color[1] - mid_color[1]) * t2)
            b = int(mid_color[2] + (end_color[2] - mid_color[2]) * t2)

        result += rgb_to_ansi(r, g, b) + char

    return result + "\033[0m"
    
def gradient_tutu(text):
    def rgb_to_ansi(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    start_color = (255, 192, 203)  # 🌸 Hồng phấn
    mid_color   = (152, 251, 152)  # 🌿 Mint nhạt
    end_color   = (255, 255, 102)  # 💛 Vàng chanh pastel

    steps = len(text)
    result = ""

    for i, char in enumerate(text):
        t = i / (steps - 1 if steps > 1 else 1)

        if t < 0.5:
            t2 = t / 0.5
            r = int(start_color[0] + (mid_color[0] - start_color[0]) * t2)
            g = int(start_color[1] + (mid_color[1] - start_color[1]) * t2)
            b = int(start_color[2] + (mid_color[2] - start_color[2]) * t2)
        else:
            t2 = (t - 0.5) / 0.5
            r = int(mid_color[0] + (end_color[0] - mid_color[0]) * t2)
            g = int(mid_color[1] + (end_color[1] - mid_color[1]) * t2)
            b = int(mid_color[2] + (end_color[2] - mid_color[2]) * t2)

        result += rgb_to_ansi(r, g, b) + char

    return result + "\033[0m"
    
def inp(text, colors=None):
    if not colors:
        # Default gradient màu tím - xanh biển - xanh lá
        colors = [129, 93, 57, 63, 69, 75, 81, 87, 93, 99, 105, 111, 117, 123]
    result = ""
    for i, c in enumerate(text):
        color = colors[i % len(colors)]
        result += f"\033[38;5;{color}m{c}"
    return result + "\033[0m"
    
unicode_invisible = ("ㅤ")

def gradient(text, start_color=(255, 0, 255), end_color=(0, 255, 255)):
    result = ""
    length = len(text)
    for i, char in enumerate(text):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / (length - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / (length - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / (length - 1))
        result += f"\033[38;2;{r};{g};{b}m{char}"
    result += "\033[0m"  # Reset màu về mặc định
    return result
    
# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Banner
    banner = (gradient("""                 ╭────────────────────────────────────────────────╮
                 │                                                │
                 │         ╦  ╦╔═╗╦ ╦╔╦╗       ╔╦╗╔═╗╔═╗╦         │
                 │         ║  ║║ ╦╠═╣ ║   ───   ║ ║ ║║ ║║         │
                 │         ╩═╝╩╚═╝╩ ╩ ╩         ╩ ╚═╝╚═╝╩═╝       │
                 │                                                │
                 ╰────────────────────────────────────────────────╯"""))
    may_anh = (gradient("""
                    ╔═                                        ═╗
                      ┌──────────────────────────────────────┐
                      │   Credits : Light - Lê Hoàng Giang   │
                      └──────────────────────────────────────┘
                    ╚═                                        ═╝"""))
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner + may_anh)
# Check if running on Termux
def check_termux():
    try:
        subprocess.run(["termux-info"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except:
        return False

# System information
def system_info():
    print(f"\n\033[1;32m[THÔNG TIN HỆ THỐNG]")
    try:
        print(gradient_2(f"OS: {platform.system()} {platform.release()}"))
        print(gradient_2(f"Processor: {platform.processor() or 'Không xác định'}"))
        print(gradient_2(f"CPU Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical"))
        print(gradient_2(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB"))
        print(gradient_2(f"Available RAM: {round(psutil.virtual_memory().available / (1024**3), 2)} GB"))
        
        # Thêm try-except cho CPU usage
        try:
            print(gradient_2(f"Current CPU Usage: {psutil.cpu_percent()}%"))
        except:
            print(gradient_2("Current CPU Usage: Không thể đọc (thiếu quyền)"))
            
        try:
            print(gradient_2(f"Current RAM Usage: {psutil.virtual_memory().percent}%"))
        except:
            print(gradient_2("Current RAM Usage: Không thể đọc (thiếu quyền)"))
            
    except Exception as e:
        print(f"\033[1;31mKhông thể đọc thông tin hệ thống: {str(e)}")

# Clean memory cache (works without root on Linux/Android)
def clean_memory():
    try:
        print(f"{Colors.OKBLUE}\n[+] Cleaning memory cache...{Colors.ENDC}")
        # Sync filesystem to prevent data loss
        os.sync()
        # Drop caches (works without root on some systems)
        with open('/proc/sys/vm/drop_caches', 'w') as f:
            f.write('3\n')
        print(f"{Colors.OKGREEN}[✓] Memory cache cleaned successfully{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Couldn't clean memory cache (partial success): {str(e)}{Colors.ENDC}")

# Optimize swap usage
def optimize_swap():
    try:
        print(f"{Colors.OKBLUE}\n[+] Optimizing swap usage...{Colors.ENDC}")
        # Check if swap is enabled
        swap_result = subprocess.run(["free", "-m"], capture_output=True, text=True)
        if "Swap" in swap_result.stdout:
            # Adjust swappiness (lower value means less swapping)
            with open('/proc/sys/vm/swappiness', 'w') as f:
                f.write('10\n')
            print(f"{Colors.OKGREEN}[✓] Swap optimized (swappiness set to 10){Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] No swap partition found{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Couldn't optimize swap: {str(e)}{Colors.ENDC}")

# Trim filesystems (especially helpful for flash storage)
def trim_filesystems():
    try:
        print(f"{Colors.OKBLUE}\n[+] Running TRIM on filesystems...{Colors.ENDC}")
        # Find all mounted filesystems
        with open('/proc/mounts', 'r') as f:
            mounts = f.readlines()
        
        trimmed = False
        for mount in mounts:
            if 'ext4' in mount or 'f2fs' in mount or 'vfat' in mount:
                dev = mount.split()[0]
                try:
                    subprocess.run(["fstrim", "-v", mount.split()[1]], check=True)
                    trimmed = True
                except:
                    continue
        
        if trimmed:
            print(f"{Colors.OKGREEN}[✓] Filesystems trimmed successfully{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] No supported filesystems found for TRIM{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Couldn't trim filesystems: {str(e)}{Colors.ENDC}")

# Kill background processes consuming resources
def kill_resource_hogs():
    try:
        print(f"{Colors.OKBLUE}\n[+] Identifying and killing resource hogs...{Colors.ENDC}")
        
        # Get all processes
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by CPU and memory usage
        cpu_hogs = sorted(processes, key=lambda p: p.info['cpu_percent'], reverse=True)
        mem_hogs = sorted(processes, key=lambda p: p.info['memory_percent'], reverse=True)
        
        # Kill top resource consumers (excluding system and our own process)
        killed = 0
        our_pid = os.getpid()
        
        for proc in cpu_hogs[:5] + mem_hogs[:5]:
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                # Skip system processes and our own process
                if pid == 1 or pid == our_pid or name in ['systemd', 'init', 'kthreadd']:
                    continue
                
                # Skip if not using significant resources
                if proc.info['cpu_percent'] < 5 and proc.info['memory_percent'] < 1:
                    continue
                
                print(f"Killing process {name} (PID: {pid}) - CPU: {proc.info['cpu_percent']}%, MEM: {proc.info['memory_percent']}%")
                os.kill(pid, signal.SIGTERM)
                killed += 1
            except:
                continue
        
        if killed > 0:
            print(f"{Colors.OKGREEN}[✓] Killed {killed} resource-hogging processes{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] No non-essential resource hogs found{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Error killing processes: {str(e)}{Colors.ENDC}")

# Optimize TCP/IP stack for better network performance
def optimize_network():
    try:
        print(f"{Colors.OKBLUE}\n[+] Optimizing network settings...{Colors.ENDC}")
        
        # Get current settings
        def get_sysctl(setting):
            try:
                return subprocess.run(["sysctl", "-n", setting], capture_output=True, text=True).stdout.strip()
            except:
                return None
        
        # Set new settings
        def set_sysctl(setting, value):
            try:
                subprocess.run(["sysctl", "-w", f"{setting}={value}"], check=True)
                return True
            except:
                return False
        
        # TCP optimizations
        settings = {
            'net.ipv4.tcp_window_scaling': '1',
            'net.ipv4.tcp_timestamps': '1',
            'net.ipv4.tcp_sack': '1',
            'net.ipv4.tcp_fack': '1',
            'net.core.rmem_max': '4194304',
            'net.core.wmem_max': '4194304',
            'net.core.rmem_default': '4194304',
            'net.core.wmem_default': '4194304',
            'net.ipv4.tcp_rmem': '4096 87380 4194304',
            'net.ipv4.tcp_wmem': '4096 65536 4194304',
            'net.ipv4.tcp_congestion_control': 'cubic',
            'net.ipv4.tcp_mtu_probing': '1',
            'net.ipv4.tcp_slow_start_after_idle': '0'
        }
        
        success = 0
        for setting, value in settings.items():
            if set_sysctl(setting, value):
                success += 1
        
        if success > 0:
            print(f"{Colors.OKGREEN}[✓] Optimized {success}/{len(settings)} network parameters{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] Couldn't modify network parameters (no root?){Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Network optimization failed: {str(e)}{Colors.ENDC}")

# Adjust process priorities
def adjust_priorities():
    try:
        print(f"{Colors.OKBLUE}\n[+] Adjusting process priorities...{Colors.ENDC}")
        
        # Get foreground app (Android only)
        foreground_app = None
        if check_termux():
            try:
                output = subprocess.run(["termux-am", "get-foreground-app"], capture_output=True, text=True).stdout
                if "packageName" in output:
                    foreground_app = output.split('"packageName": "')[1].split('"')[0]
            except:
                pass
        
        # Get all processes
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'nice']):
            try:
                processes.append(proc)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        adjusted = 0
        our_pid = os.getpid()
        
        for proc in processes:
            try:
                pid = proc.info['pid']
                name = proc.info['name']
                current_nice = proc.info['nice']
                
                # Skip system processes and our own process
                if pid == 1 or pid == our_pid or name in ['systemd', 'init', 'kthreadd']:
                    continue
                
                # Skip if already at maximum priority
                if current_nice <= -20:
                    continue
                
                # Set priority based on process type
                new_nice = 0  # Default
                
                # Higher priority for foreground app
                if foreground_app and name == foreground_app:
                    new_nice = -15
                # Lower priority for background services
                elif 'com.android' in name or 'service' in name.lower():
                    new_nice = 10
                # Medium priority for other apps
                else:
                    new_nice = 0
                
                # Apply new priority
                if new_nice != current_nice:
                    os.nice(new_nice - current_nice)
                    adjusted += 1
            except:
                continue
        
        if adjusted > 0:
            print(f"{Colors.OKGREEN}[✓] Adjusted priority for {adjusted} processes{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] No process priorities adjusted{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Error adjusting priorities: {str(e)}{Colors.ENDC}")

# Disable animations (works on some Android devices without root)
def disable_animations():
    try:
        print(f"{Colors.OKBLUE}\n[+] Attempting to disable animations...{Colors.ENDC}")
        
        if check_termux():
            settings = {
                'window_animation_scale': '0',
                'transition_animation_scale': '0',
                'animator_duration_scale': '0'
            }
            
            changed = 0
            for setting, value in settings.items():
                try:
                    subprocess.run(["termux-am", "settings", "put", "global", setting, value], check=True)
                    changed += 1
                except:
                    continue
            
            if changed > 0:
                print(f"{Colors.OKGREEN}[✓] Disabled {changed}/3 animation scales{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[!] Couldn't disable animations (no permission){Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] Animation control requires Termux{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}[!] Error disabling animations: {str(e)}{Colors.ENDC}")

# Continuous monitoring thread
def monitor_system():
    while monitoring:
        try:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory().percent
            temp = psutil.sensors_temperatures().get('cpu-thermal', [psutil._common.shwtemp('', 0, 0)])[0].current
            
            print(f"\n{Colors.HEADER}[SYSTEM MONITOR]{Colors.ENDC}")
            print(f"CPU Usage: {cpu}% | RAM Usage: {mem}% | Temp: {temp}°C")
            
            # If thresholds are exceeded, take action
            if cpu > 85 or mem > 85:
                print(f"{Colors.WARNING}[!] High resource usage detected!{Colors.ENDC}")
                kill_resource_hogs()
                clean_memory()
        except:
            pass
        
        time.sleep(5)
# Main menu
def main_menu():
    print(gradient_1(f"\n[MAIN MENU]"))
    print(gradient_tutu("1. Run All Optimizations - Tối Ưu Tất Cả"))
    print(gradient_tutu("2. Clean Memory Cache - Dọn Dẹp Bộ Nhớ Đệm"))
    print(gradient_tutu("3. Optimize Swap Usage - Tối Ưu Hoá Swap"))
    print(gradient_tutu("4. Trim Filesystems - Dọn Dẹp Hệ Thống Tệp"))
    print(gradient_tutu("5. Kill Resource Hogs - Tắt Các Tiến Trình Đang Chạy"))
    print(gradient_tutu("6. Optimize Network - Tối Ưu Mạng"))
    print(gradient_tutu("7. Adjust Process Priorities - Điều Chỉnh Ưu Tiên Tiến Trình"))
    print(gradient_tutu("8. Disable Animations - Tắt Hiệu Ứng Hình Ảnh"))
    print(gradient_tutu("9. Start Continuous Monitoring - Bắt Đầu Giám Sát Liên Tục"))
    print(gradient_tutu("10. System Information - Thông Tin Hệ Thống"))
    print(gradient_1("0. Exit"))
    
    choice = input("\nSelect an option: ")
    return choice

# Main function
def main():
    global monitoring
    
    if not check_termux():
        print(f"{Colors.FAIL}[!] This tool is designed to run in Termux on Android{Colors.ENDC}")
        print(f"{Colors.WARNING}Some features may not work outside Termux{Colors.ENDC}")
    
    system_info()
    
    monitoring = False
    monitor_thread = None
    
    while True:
        print(gradient("-"*50))
        choice = main_menu()
        
        if choice == '1':
            clean_memory()
            optimize_swap()
            trim_filesystems()
            kill_resource_hogs()
            optimize_network()
            adjust_priorities()
            disable_animations()
        elif choice == '2':
            clean_memory()
        elif choice == '3':
            optimize_swap()
        elif choice == '4':
            trim_filesystems()
        elif choice == '5':
            kill_resource_hogs()
        elif choice == '6':
            optimize_network()
        elif choice == '7':
            adjust_priorities()
        elif choice == '8':
            disable_animations()
        elif choice == '9':
            if not monitoring:
                monitoring = True
                monitor_thread = threading.Thread(target=monitor_system, daemon=True)
                monitor_thread.start()
                print(f"{Colors.OKGREEN}[✓] Started continuous monitoring{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[!] Monitoring is already running{Colors.ENDC}")
        elif choice == '10':
            system_info()
        elif choice == '0':
            if monitoring:
                monitoring = False
                if monitor_thread:
                    monitor_thread.join(timeout=1)
            print(f"{Colors.OKGREEN}\n[✓] Exiting... Goodbye!{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}[!] Invalid choice{Colors.ENDC}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Colors.FAIL}\n[!] Interrupted by user{Colors.ENDC}")
        sys.exit(0)