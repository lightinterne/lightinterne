import json
import os,time
import cloudscraper
import requests
import socket
import subprocess
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from colorama import Fore, init
import sys
import requests



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
    
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("\033[1;31mMạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")

kiem_tra_mang()
def input_with_box(prompt):
    user_input = input(prompt)
    box_width = len(user_input) + 2
    print("╭" + "─" * box_width + "╮")
    print("│ " + user_input + " │")
    print("╰" + "─" * box_width + "╯")
    return user_input
#╭────────────╮
#│   GIANG    │
#╰────────────╯
banner = gradient(f"""
                 ╭────────────────────────────────────────────────╮
                 │                                                │
                 │         ╦  ╦╔═╗╦ ╦╔╦╗       ╔╦╗╔═╗╔═╗╦         │
                 │         ║  ║║ ╦╠═╣ ║   ───   ║ ║ ║║ ║║         │
                 │         ╩═╝╩╚═╝╩ ╩ ╩         ╩ ╚═╝╚═╝╩═╝       │
                 │                                                │
                 ╰────────────────────────────────────────────────╯
""")
may_anh = gradient("""                    ╔═                                        ═╗
                      ┌──────────────────────────────────────┐
                      │   Credits : Light - Lê Hoàng Giang   │
                      └──────────────────────────────────────┘
                    ╚═                                        ═╝""")
os.system('cls' if os.name== 'nt' else 'clear')
print(banner + may_anh)
print(gradient_tutu("""╔═════════════════════════════════╗
║        CHỌN CÁCH VÀO TOOL       ║
╚═════════════════════════════════╝"""))

    # Nhập auth
def nhap_hoac_doc_token():
    try:
        open("Authorization.txt", "x").close()
        open("token.txt", "x").close()
    except:
        pass

    if os.path.getsize("Authorization.txt") > 0 and os.path.getsize("token.txt") > 0:
        print(gradient_1("║ => Nhập 1 Để Tiếp Tục Với Authorization Cũ"))
        print(gradient_1("║"))
        print(gradient_1("║ => Nhập 2 Để Thay Đổi Authorization Mới"))
        select = input_with_box("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập Lựa Chọn\033[1;36m ] \033[1;31m- \033[1;36m[ \033[1;32mLight - Lê Hoàng Giang \033[1;36m]\n\033[1;31m│\n╰─➤\033[1;33m  """)
        if select == "1":
            with open("Authorization.txt", "r") as f:
                author = f.read().strip()
            with open("token.txt", "r") as f:
                token = f.read().strip()
        else:
            author = input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mAuthorization\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """).strip()
            token = input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mToken\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """).strip()
            with open("Authorization.txt", "w") as f:
                f.write(author)
            with open("token.txt", "w") as f:
                f.write(token)
    else:
        author = input("""\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mAuthorization\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """).strip()
        token = input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mToken\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """).strip()
        with open("Authorization.txt", "w") as f:
            f.write(author)
        with open("token.txt", "w") as f:
            f.write(token)
    return author, token
author, token = nhap_hoac_doc_token()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}

scraper = cloudscraper.create_scraper()
def chonacc():
    json_data = {}
    try:
      response = scraper.get(
        'https://gateway.golike.net/api/tiktok-account',
    
        headers=headers,
        json=json_data
     ).json()
      return response
    except Exception:
      sys.exit()

def nhannv(account_id):
    try:
        params = {
            'account_id': account_id,
            'data': 'null',
        }
   
        response = scraper.get(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',
            headers=headers,
            params=params,
            json={}
        )
        return response.json()
    except Exception:
      sys.exit()

def hoanthanh(ads_id, account_id):
    try:
        json_data = {
            'ads_id': ads_id,
            'account_id': account_id,
            'async': True,
            'data': None,
        }

        response = scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
            headers=headers,
            json=json_data,
            timeout=6
        )
        return response.json()
    except Exception:
      sys.exit()

def baoloi(ads_id, object_id, account_id, loai):
    try:
        json_data1 = {
            'description': 'Tôi đã làm Job này rồi',
            'users_advertising_id': ads_id,
            'type': 'ads',
            'provider': 'tiktok',
            'fb_id': account_id,
            'error_type': 6,
        }

        scraper.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1)

        json_data2 = {
            'ads_id': ads_id,
            'object_id': object_id,
            'account_id': account_id,
            'type': loai,
        }

        scraper.post(
            'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
            headers=headers,
            json=json_data2,
        )
    except Exception:
      sys.exit()
      

khung = gradient_tutu("""\n╔═════════════════════════════════╗
║        Danh Sách Acc Hiện Có    ║
╚═════════════════════════════════╝""")
# Gọi chọn tài khoản một lần và xử lý lỗi nếu có
chontktiktok = chonacc()

def dsacc():
  if chontktiktok.get("status") != 200:  
    print("\033[1;31mAuthorization Or Token Warning❗")
    quit()
  os.system('cls' if os.name== 'nt' else 'clear')
  print(banner + may_anh + khung)
  for i in range(len(chontktiktok["data"])):
    print(gradient_2(f'[{i+1}] {chontktiktok["data"][i]["nickname"]} |✅ Online'))
dsacc() 

vien = gradient_tutu("═════════════════════════════════════════════════")
while True:
  try:
    luachon = int(input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mAcc Muốn Chạy\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """))
    print(vien)
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;31mSai Định Dạng, Nhập Lại\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;31mSai Định Dạng ") 
while True:
  try:
    delay = int(input(f"""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mDelay\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """))
    break
  except:
    print("\033[1;31mSai Định Dạng ")
while True:
  try: 
    doiacc = int(input(f"\033[1;32mThất Bại Bao Nhiêu Lần Thì Đổi Acc: \033[1;33m"))
    break
  except:
    print("\033[1;31m🚀 Nhập Vào 1 Số 🚀")  
print(gradient_tutu("""╔═════════════════════════════════╗
║     CHỌN NHIỆM VỤ KIẾM TIỀN     ║
╚═════════════════════════════════╝"""))
print(gradient_1("║ => [1] Nhiệm Vụ Follow"))
print(gradient_1("║ => [2] Nhiệm Vụ Tim"))
print(gradient_1("║ => [3] Cả Follow Và Tim"))
while True:
    try:
        print(vien)
        loai_nhiem_vu = int(input("""\n\033[1;31m╭─────\033[1;36m[ \033[1;32mNhập \033[1;33mNhiệm Vụ\033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """))
        if loai_nhiem_vu in [1, 2, 3]:
            break
        else:
            print("\033[1;31mVui lòng chọn số từ 1 đến 3!")
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số.")  
print(vien)
x_like, y_like, x_follow, y_follow = None, None, None, None
print(gradient_tutu("""╔═════════════════════════════════╗
║       CHỌN CÁCH CHẠY TOOL      ║
╚═════════════════════════════════╝"""))
print(gradient_1("║ => [1] ADB " + "[ Lỗi ]"))
print(gradient_1("║ => [2] Auto Click"))
adbyn = input(f"""\n\033[1;31m╭─────\033[1;36m[ \033[\033[1;33mNhập Lựa Chọn \033[1;36m ] \033[1;31m- \033[1;36m[\033[1;32m Light - Lê Hoàng Giang\033[1;36m ]\033[1;31m
│ 
╰─➤\033[1;33m  """)

if adbyn == "1":
    def setup_adb():
      config_file = "adb_config.txt"
      like_coords_file = "toa_do_tim.txt"
      follow_coords_file = "toa_do_follow.txt"

    # Nhập IP và port ADB
      print(f"{Fore.MAGENTA}═══════════════════════════════════")
      print("\033[1;36mBạn có thể xem video hướng dẫn kết nối ADB ở trên Youtube!!! ")
      ip = input("\033[1;32mNhập IP của thiết bị ví dụ (192.168.1.2): \033[1;33m")
      adb_port = input("\033[1;32mNhập port của thiết bị ví dụ (39327): \033[1;33m")

      # Kiểm tra và đọc tọa độ từ file nếu tồn tại
      x_like, y_like, x_follow, y_follow = None, None, None, None
    
      if os.path.exists(like_coords_file):
           with open(like_coords_file, "r") as f:
              coords = f.read().split("|")
              if len(coords) == 2:
                   x_like, y_like = coords
                   print(f"\033[1;32mĐã tìm thấy tọa độ nút tim: X={x_like}, Y={y_like}")
    
      if os.path.exists(follow_coords_file):
          with open(follow_coords_file, "r") as f:
               coords = f.read().split("|")
               if len(coords) == 2:
                   x_follow, y_follow = coords
                   print(f"\033[1;32mĐã tìm thấy tọa độ nút follow: X={x_follow}, Y={y_follow}")
      if not os.path.exists(config_file):
           print("\033[1;36mLần đầu chạy, nhập mã ghép nối (6 SỐ) và port ghép nối.\033[0m")
           pair_code = input("\033[1;32mNhập mã ghép nối 6 số ví dụ (322763): \033[1;33m")
           pair_port = input("\033[1;32mNhập port ghép nối ví dụ (44832): \033[1;33m")

           with open(config_file, "w") as f:
               f.write(f"{pair_code}|{pair_port}")
      else:
          with open(config_file, "r") as f:
               pair_code, pair_port = [s.strip() for s in f.read().split("|")]
  
      print("\n\033[1;36m Đang ghép nối với thiết bị\033[0m")
      os.system(f"adb pair {ip}:{pair_port} {pair_code}")
      time.sleep(2)
  
      print("\033[1;36mĐang kết nối ADB\033[0m")
      os.system(f"adb connect {ip}:{adb_port}")
      time.sleep(2)
  
      devices = os.popen("adb devices").read()
      if ip not in devices:
        print(f"{Fore.RED}Kết nối thất bại{Fore.WHITE}")
        exit()
    

       # Yêu cầu nhập tọa độ nếu chưa có
      print("\033[1;39m╔═════════════════════════════════╗")
      print("\033[1;39m║     \033[1;36m NHẬP TỌA ĐỘ        \033[1;39m║")
      print("\033[1;39m╚═════════════════════════════════╝")
    
      if loai_nhiem_vu in [1, 3] and (x_follow is None or y_follow is None):
           x_follow = input("\033[1;32mNhập tọa độ X của nút follow: \033[1;33m")
           y_follow = input("\033[1;32mNhập tọa độ Y của nút follow: \033[1;33m")
           with open(follow_coords_file, "w") as f:
               f.write(f"{x_follow}|{y_follow}")
    
      if loai_nhiem_vu in [2, 3] and (x_like is None or y_like is None):
           x_like = input("\033[1;32mNhập tọa độ X của nút tim: \033[1;33m")
           y_like = input("\033[1;32mNhập tọa độ Y của nút tim: \033[1;33m")
           with open(like_coords_file, "w") as f:
              f.write(f"{x_like}|{y_like}")

      return x_like, y_like, x_follow, y_follow

# Khi gọi hàm setup_adb()
    x_like, y_like, x_follow, y_follow = setup_adb()
elif adbyn == "2":
    pass
# Thêm phần chọn loại nhiệm vụ sau khi chọn tài khoản và trước khi bắt đầu làm nhiệm vụ
   
dem = 0
start_time = time.time()
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

print(banner + may_anh)
print(gradient_tutu("""╔═════════════════════════════════════╗
║        Bắt Đầu Kiếm Tiền💸          ║
╚═════════════════════════════════════╝"""))

while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
        print(f"{Fore.WHITE}════════════════════════════════════════════════════════")
        print(f"\033[1;31mAcc TikTok {dsaccloi} Bị Lỗi, Nhả Job")
        print(f"{Fore.WHITE}════════════════════════════════════════════════════════")
        dsacc()
        while True:
            try:
                print(f"{Fore.WHITE}════════════════════════════════════════════════════")
                luachon = int(input(gradient_2("Chọn Tài Khoản Để Tiếp Tục: ")))
                while luachon > len((chontktiktok)["data"]):
                    luachon = int(input("\033[1;31mAcc Này Chưa Được Cấu Hình, Nhập Lại: \033[1;33m"))
                account_id = chontktiktok["data"][luachon - 1]["id"]
                checkdoiacc = 0
                os.system('cls' if os.name== 'nt' else 'clear')
                for h in banner:
                    print(h,end = "")
                break  
            except:
                print("\033[1;31mSai Định Dạng !!!")
    print('\033[1;32mĐang Tìm Job, Đợi Xíu Nhen...', end="\r")
    max_retries = 3
    retry_count = 0
    nhanjob = None

    while retry_count < max_retries:
        try:
            nhanjob = nhannv(account_id)
            if nhanjob and nhanjob.get("status") == 200 and nhanjob["data"].get("link") and nhanjob["data"].get("object_id"):
                break
            else:
                retry_count += 1
                time.sleep(2)
        except Exception as e:
            retry_count += 1
            time.sleep(1)

    if not nhanjob or retry_count >= max_retries:
        continue

    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    job_type = nhanjob["data"]["type"]

    # Kiểm tra loại nhiệm vụ
    if (loai_nhiem_vu == 1 and job_type != "follow") or \
       (loai_nhiem_vu == 2 and job_type != "like") or \
       (job_type not in ["follow", "like"]):
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Mở link và kiểm tra lỗi
    try:
        if adbyn == "1":
            os.system(f'adb shell am start -a android.intent.action.VIEW -d "{link}" > /dev/null 2>&1')
        else:
            #os.system(f"termux-open-url {link}")
            subprocess.run(["termux-open-url", link])
        
        for remaining in range(3, 0, -1):
            time.sleep(1)
        print("\r" + " " * 30 + "\r", end="")

    except Exception as e:
        baoloi(ads_id, object_id, account_id, job_type)
        continue

    # Thực hiện thao tác ADB
    if job_type == "like" and adbyn == "1" and x_like and y_like:
        os.system(f"adb shell input tap {x_like} {y_like}")
    elif job_type == "follow" and adbyn == "1" and x_follow and y_follow:
        os.system(f"adb shell input tap {x_follow} {y_follow}")

    # Đếm ngược delay
    for remaining_time in range(delay, -1, -1):
        color = "\033[1;36m" if remaining_time % 2 == 0 else "\033[1;33m"
        print(f"\r{color} Delay Job {remaining_time}s           ", end="")
        time.sleep(1)
    
    print("\r                          \r", end="") 
    print("\033[1;36m Đang Nhận Tiền...  ",end = "\r")

    # Hoàn thành job
    max_attempts = 2
    attempts = 0
    nhantien = None
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien and nhantien.get("status") == 200:
                break
        except:
            pass  
        attempts += 1

    if nhantien and nhantien.get("status") == 200:
        dem += 1
        tien = nhantien["data"]["prices"]
        tong += tien
        local_time = time.localtime()
        hour = local_time.tm_hour
        minute = local_time.tm_min
        second = local_time.tm_sec
        h = hour
        m = minute
        s = second
        if hour < 10:
            h = "0" + str(hour)
        if minute < 10:
            m = "0" + str(minute)
        if second < 10:
            s = "0" + str(second)
                                      
        chuoi = gradient_2(f"Light - Tool | [ {dem} ] | {job_type} | + {tien} | Tổng Tiền: {tong} | Time: {h}:{m}:{s}")

        print("                                                    ", end="\r")
        print(chuoi)

# 👇 In sau mỗi 10 job
    if dem % 10 == 0:
        elapsed = int(time.time() - start_time)
        h = elapsed // 3600
        m = (elapsed % 3600) // 60
        s = elapsed % 60
        thongtin = f"\033[1;32m📊 Tổng nhiệm vụ: \033[1;33n{dem}\033[1;35m | \033[1;32m⏱️ Thời gian:\033[1;33m {h:02}:{m:02}:{s:02} \033[1;35m| 💸 \033[1;32mTổng tiền nhận: \033[1;33m{tong}đ"
        print(gradient_1('='*84))
        print(thongtin)
        print(gradient_1('='*84))

        time.sleep(0.7)
        checkdoiacc = 0
    else:
        try:
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            print("                                              ", end="\r")
            print("\033[1;31mBỏ qua job", end="\r")
            sleep(1)
            checkdoiacc += 1
        except:
            pass