import requests
import random
import os

def download_wallhaven_image(query):
    print(f"🔍 Đang tìm ảnh thể loại: {query}")
    search_url = f"https://wallhaven.cc/api/v1/search?q={query}&purity=100"

    try:
        res = requests.get(search_url)
        data = res.json()

        if data["data"]:
            # Chọn ngẫu nhiên 1 ảnh trong kết quả
            img = random.choice(data["data"])
            image_url = img["path"]

            print("🌐 Ảnh:", image_url)

            # Tải ảnh về
            image_data = requests.get(image_url)
            if image_data.status_code == 200:
                if not os.path.exists("downloads"):
                    os.makedirs("downloads")

                file_name = f"{query}_{random.randint(1000,9999)}.jpg"
                path = os.path.join("downloads", file_name)

                with open(path, 'wb') as f:
                    f.write(image_data.content)

                print(f"✅ Đã tải ảnh về: {path}")
            else:
                print("❌ Không tải được ảnh.")
        else:
            print("❌ Không tìm thấy ảnh nào cho từ khóa:", query)
    except Exception as e:
        print("⚠️ Lỗi:", e)

if __name__ == "__main__":
    the_loai = input("👉 Bạn muốn tải ảnh thể loại gì?: ").strip()
    so_luong = input("📸 Bạn muốn tải bao nhiêu ảnh?: ").strip()

    try:
        count = int(so_luong)
        for _ in range(count):
            download_wallhaven_image(the_loai)
    except:
        print("⚠️ Số lượng không hợp lệ.")