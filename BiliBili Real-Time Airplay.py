import requests
import time
import datetime

# API 将bvid后的BV号替换成需要的BV号即可
api_url = "https://api.bilibili.com/x/web-interface/view?bvid=BV1cMSUYiE5m"

# 记录log文件名
log_file = "bilibili_view_log.txt"

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}

def fetch_view_count():
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("stat", {}).get("view")
    except Exception:
        return None

def log_view_count(view_count):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{current_time} - {view_count}"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")
    print(log_entry)

if __name__ == "__main__":
    print("开始记录播放量 按键 Ctrl+C 结束")
    try:
        while True:
            view_count = fetch_view_count()
            if view_count is not None:
                log_view_count(view_count)
            else:
                print("未能获取到播放量")
            time.sleep(10) # 获取间隔秒数
    except KeyboardInterrupt:
        print("\n记录已结束")

