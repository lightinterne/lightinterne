import os
import time
import requests
import warnings

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
    
warnings.filterwarnings("ignore")

def clear(): os.system("clear")

def banner():
    clear()
    print(gradient("""                 ╭────────────────────────────────────────────────╮
                 │                                                │
                 │         ╦  ╦╔═╗╦ ╦╔╦╗       ╔╦╗╔═╗╔═╗╦         │
                 │         ║  ║║ ╦╠═╣ ║   ───   ║ ║ ║║ ║║         │
                 │         ╩═╝╩╚═╝╩ ╩ ╩         ╩ ╚═╝╚═╝╩═╝       │
                 │                                                │
                 ╰────────────────────────────────────────────────╯"""))
    print(gradient("""
                    ╔═                                        ═╗
                      ┌──────────────────────────────────────┐
                      │   Credits : Light - Lê Hoàng Giang   │
                      └──────────────────────────────────────┘
                    ╚═                                        ═╝"""))

def format_money(xu):
    return f"+{xu} xu"

def get_authorization():
    file = "Authorization.txt"
    if os.path.exists(file):
        with open(file, "r") as f:
            token = f.read().strip()
            if token:
                return token
    while True:
        token = input("\033[1;32mNhập Authorization:\033[1;33m ").strip()
        if token:
            with open(file, "w") as f:
                f.write(token)
            return token

def get_snapchat_accounts(headers):
    try:
        res = requests.get("https://gateway.golike.net/api/snapchat-account", headers=headers, timeout=10)
        return res.json()
    except:
        return None

def show_accounts(data):
    print("\033[1;36m┌────┬──────────────────────────────┐")
    print("│ \033[1;33mSTT\033[1;36m│\033[1;32m Tên tài khoản Snapchat      \033[1;36m │")
    print("\033[1;36m├────┼──────────────────────────────┤")
    for i, acc in enumerate(data['data']):
        stt = str(i + 1).rjust(2)
        name = acc['snap_username'][:28].ljust(28)
        print(f"│\033[1;33m {stt} \033[1;36m│\033[1;32m {name} \033[1;36m│")
    print("└────┴──────────────────────────────┘")

def select_account(data):
    try:
        stt = int(input("\033[1;32mNhập Lựa Chọn:\033[1;33m ")) - 1
        account = data["data"][stt]
        print(f"\n👉 Bạn đang chọn tài khoản: {account['snap_username']}\n")
        return account["id"]
    except:
        print("⚠ Lựa chọn không hợp lệ.")
        return None

def get_jobs(account_id, headers):
    try:
        url = f"https://gateway.golike.net/api/advertising/publishers/snapchat/jobs?account_id={account_id}&data=null"
        res = requests.get(url, headers=headers, timeout=10)
        return res.json()
    except:
        return None
        
def complete_job(account_id, ads_id, headers):
    payload = {
        "ads_id": ads_id,
        "account_id": account_id,
        "async": True,
        "data": None
    }
    try:
        res = requests.post("https://gateway.golike.net/api/advertising/publishers/snapchat/complete-jobs",
                            headers=headers, json=payload, timeout=10)
        return res.json()
    except:
        return {"status": 0}

def skip_job(account_id, ads_id, object_id, job_type, headers):
    payload = {
        "ads_id": ads_id,
        "object_id": object_id,
        "account_id": account_id,
        "type": job_type
    }
    try:
        requests.post("https://gateway.golike.net/api/advertising/publishers/snapchat/skip-jobs",
                      headers=headers, json=payload, timeout=10)
    except:
        pass

def print_table(jobs_table):
    clear()
    print("\033[1;36m┌──────┬────────────────────────────────┬────────┬────────────┬──────────────┐")
    print("│\033[1;33m STT  \033[1;36m│\033[1;33m Link Job \033[1;36m                      │\033[1;33m Type  \033[1;36m │\033[1;33m Xu Nhận \033[1;36m   │\033[1;33m Tổng VND   \033[1;36m  │")
    print("├──────┼────────────────────────────────┼────────┼────────────┼──────────────┤")
    for job in jobs_table:
        stt = str(job['stt']).rjust(4)
        link = job['link'][:30].ljust(30)
        jtype = job['type'].ljust(6)
        coin = f"+{job['coin']} VND".ljust(10)
        total = f"{job['total']} VND".rjust(12)
        print(f"│ \033[1;33m{stt}\033[1;36m │ \033[1;32m{link}\033[1;36m │ \033[1;32m{jtype} \033[1;36m│ \033[1;35m{coin}\033[1;36m │\033[1;36m {total}\033[1;36m │")
    print("└──────┴────────────────────────────────┴────────┴────────────┴──────────────┘")

def print_final_summary(success, fail, total_coin):
    print("\n\033[1;32m🧾 Tổng hợp phiên làm việc:")
    print("──────────────────────────────────────────────")
    print(f"\033[1;32m✔ Tổng job thành công : {success}")
    print(f"\033[1;31m❌ Tổng job thất bại   : {fail}")
    print(f"\033[1;33m💰 Tổng xu đã nhận     : {total_coin} xu")
    print(f"\033[1;35m📦 Tổng job xử lý      : {success + fail}")
    print("──────────────────────────────────────────────")

def do_jobs(headers, account_id, delay, allowed_types, fail_limit):
    fail_count = 0
    success_count = 0
    total_fail = 0
    job_counter = 0
    jobs_table = []
    previous_job = None
    total_coin = 0

    while True:
        try:
            job = get_jobs(account_id, headers)
            if not job or job.get("status") != 200 or "data" not in job or not job["data"]:
                print("\033[1;31m⚠ Không có job hoặc lỗi kết nối.")
                fail_count += 1
                total_fail += 1
                if fail_count >= fail_limit:
                    print("\033[1;31mĐạt Số Lượng Lỗi!")
                    break
                time.sleep(3)
                continue

            job_data = job["data"]
            job_type = job_data["type"]
            job_link = job_data.get("link", "")
            ads_id = job_data["id"]
            object_id = job_data["object_id"]

            if job_type not in allowed_types or not job_link:
                skip_job(account_id, ads_id, object_id, job_type, headers)
                continue

            if previous_job and previous_job.get("link") == job_link:
                skip_job(account_id, ads_id, object_id, job_type, headers)
                continue

            previous_job = job_data
            job_counter += 1

            print(f"\n🔗 Mở link: {job_link}")
            os.system(f"termux-open-url '{job_link}'")
            for i in range(delay, 0, -1):
                print(f"Delay Giây {i}s...", end="\r")
                time.sleep(1)

            result = complete_job(account_id, ads_id, headers)

            if result and result.get("status") == 200 and "data" in result and "prices" in result["data"]:
                coin = result["data"]["prices"]
                total_coin += coin
                success_count += 1
                fail_count = 0
            else:
                coin = 0
                total_fail += 1
                fail_count += 1
                skip_job(account_id, ads_id, object_id, job_type, headers)
                if fail_count >= fail_limit:
                    print("\033[1;31mĐạt Số Lượng Lỗi!")
                    break

            jobs_table.append({
                "stt": job_counter,
                "link": job_link,
                "type": job_type,
                "coin": coin,
                "total": total_coin
            })

            print_table(jobs_table)

        except KeyboardInterrupt:
            print("\n\033[1;32mStop Success Tool Snapchat Golike By Light")
            break

    print_final_summary(success_count, total_fail, total_coin)

def main():
    banner()
    token = get_authorization()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10)',
    }

    acc_data = get_snapchat_accounts(headers)
    if not acc_data or acc_data.get("status") != 200:
        print("❌ Token sai hoặc server lỗi.")
        return

    show_accounts(acc_data)
    try:
        stt = int(input("\033[1;32mNhập Lựa Chọn:\033[1;33m ")) - 1
        account_id = acc_data["data"][stt]["id"]
    except:
        print("\033[1;31m⚠ Số không hợp lệ.")
        return

    try:
        delay = int(input("\033[1;32mNhập Delay \033[1;33m(20-60)\033[1;32m:\033[1;33m "))
        fail_limit = int(input("\033[1;32mBao Nhiêu Job Lỗi Thì Dừng:\033[1;33m "))
        mode = input("\033[1;32mChọn Job \033[1;35m[ 1 FOLLOW | 2 TIM | 12 FULL ]\033[1;32m:\033[1;33m ").strip()
    except:
        print("\033[1;31m❌ Nhập sai định dạng.")
        return

    if mode == "1":
        types = ["follow"]
    elif mode == "2":
        types = ["like"]
    else:
        types = ["follow", "like"]

    do_jobs(headers, account_id, delay, types, fail_limit)

if __name__ == "__main__":
    main()