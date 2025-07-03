#==========================================================================
#|Không dc rhay admin nhé các bé, share thì cre light dỗ😛😛
#==============================================================
import requests,os, random
from time import sleep
list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0
import os, sys
import requests
import os, sys
import time
from time import strftime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
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
    
def input_with_box(prompt):
    user_input = input(prompt)
    box_width = len(user_input) + 2
    print("╭" + "─" * box_width + "╮")
    print("│ " + user_input + " │")
    print("╰" + "─" * box_width + "╯")
    return user_input
    
class REG_PAGE_PRO5_BY_LIGHT:
    def banner(self):
        os.system('title TOOL REG PAGR PRO5 + UP AVT | ĐA LUỒNG')
        os.system("cls" if os.name == "nt" else "clear")
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
        print(banner + may_anh)
    def ndp_delay_tool(self, p):
        #Anh Light Cu To 
        #Xoá Dòng Này = Con Mẹ Mày Chết Chùm
        #hé Hé
        while(p>1):
            p=p-1
            print(f'LIGHT - TOOL LO.[{p}]','     ',end='\r');sleep(1/6)
            print(f'LIGHT - TOOL LOA..[{p}]','     ',end='\r');sleep(2/6)
            print(f'LIGHT - TOOL LOAD...[{p}]','     ',end='\r');sleep(3/6)
            print(f'LIGHT - TOOL LOADI....[{p}]','     ',end='\r');sleep(4/6)
            print(f'LIGHT - TOOL LOADIN.....[{p}]','     ',end='\r');sleep(5/6)
            print(f'LIGHT - TOOL LOADING......[{p}]','     ',end='\r');sleep(6/6)
    def getthongtinfacebook(self, cookie: str):
        #Anh Light Cu To 
        #Xoá Dòng Này = Con Mẹ Mày Chết Chùm
        #hé Hé
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            print(f'\033[1;35mĐang Check Cookie..... ', end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return False
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
            return name_get,uid_get,fb_dtsg_get,jazoest_get
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
                return name_get,uid_get,fb_dtsg_get,jazoest_get
            except:
                return False
    def UpAvt(self, cookie, id_page, link_anh):
        sleep(5)
        #Anh Light Cu To 
        #Xoá Dòng Này = Conej Mày Chết Chùm
        #hé Hé
        try:
            json_upavt =  requests.get(f'https://api-ndpcutevcl.000webhostapp.com/api/upavtpage.php?cookie={cookie}&id={id_page}&link_anh={link_anh}').json()
            if json_upavt['status'] == 'success':
                return json_upavt
            else:
                return False
        except:
            return False
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        #Anh Light Cu To 
        #Xoá Dòng Này = Conej Mày Chết Chùm
        #hé Hé
        #😘😘😘
        namepage = requests.get('https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/male?count=2').json()['data'][0]['name']
        global dem
        headers_reg = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width': '979','x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation','x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY','cookie': cookie}
        data_reg = {'av': uid,'__user': uid,'__a': '1','__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo','__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u','__req': 't','__hs': '19296.HYP:comet_pkg.2.1.0.2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1006496476','__s': '1gapab:y4xv3f:2hb4os','__hsi': '7160573037096492689','__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': 'ZM7FAk6cuRcUp3imwqvHTY','__aaid': '800444344545377','__spin_r': '1006496476','__spin_b': 'trunk','__spin_t': '1667200829','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"reg auto by duykhanh","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '5903223909690825',}
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            dem+=1
            print(f'{dem} | SUCCESS | NAME FB: {name} | UID PRO5: {idpage} | NAME PRO5: {namepage}')
            return idpage
        except:
            print('\033[1;31mReg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!')
            return False
# =========================== [ START TOOL ] ===========================
dpcutevcl = REG_PAGE_PRO5_BY_LIGHT()
dpcutevcl.banner()
while True:
    stt+=1
    cookie_fb = input(f'\033[1;32m💸Nhập Cookie Facebook Thứ \033[1;33m{stt}\033[1;32m:\033[1;33m ')
    if cookie_fb == '':
        break
    checklive = dpcutevcl.getthongtinfacebook(cookie_fb)
    if checklive != False:
        print('\033[1;32mSuccess Cookie Online')
        list_clone.append(f'{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}')
        print(gradient_1('─'*50))
    else:
        stt-1
        print('Cookie '+cookie_fb.split('c_user=')[1].split(';')[0]+', Die Or Out Vui Lòng Kiểm Tra Lại!!')
# Tiến Hành Nhập Setting Reg Page
print(gradient_1('─'*50))
luachon = input_with_box(gradient_2('Bạn Có Muốn Reg Avatar Chứ? [Y/N]: '))
print(gradient_1('─'*50))
print(gradient_2('[ENTER - ĐỂ DỪNG NHẬP]'))
while True:
    stt2+=1 
    link_img = input(gradient_2(f'Nhập Link Ảnh Thứ [{stt2}]: '))
    if link_img == '':
        break
    list_img.append(link_img)
print(gradient_1('─'*50))
slpage = int(input_with_box(gradient_tutu('Bạn Muốn Reg Bao Nhiêu Acc Pro5: ')))
print(gradient_1('─'*50))
delay = int(input_with_box(gradient_tutu('Nhập Delay (Khuyến Cáo 60s~): ')))
print(gradient_1('─'*50))
# Tiến Hành Chạy Tool
dpcutevcl.banner()
print(gradient_1('─'*50))
print('\033[1;32mĐã Tìm Thấy: \033[1;33m'+str(len(list_clone))+' Cookie')
print('\033[1;32mĐã Tìm Thấy:\033[1;33m '+str(len(list_img))+' Link Image')
print(gradient_1('─'*50))
while True:
    for dulieuclone in list_clone:
        idpage = dpcutevcl.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])
        if luachon == 'Y' or luachon == 'y':
            link_anh = random.choice(list_img)
            dpcutevcl.UpAvt(str(dulieuclone).split('|')[0], idpage, link_anh)
            if dpcutevcl != False:
                print(f'\033[1;32mSuccess Avatar\033[1;33m {idpage}]')
            else:
                print(f'\033[1;31mWarning Avatar \033[1;33m{idpage}]')
        dpcutevcl.ndp_delay_tool(delay)
        if dem == slpage:
            input(f'\033[1;32mSUCCESS\033[1;33m {dem}, \033[1;32mPAGE </> ENTER ĐỂ OUT TOOL!!!')
            exit()