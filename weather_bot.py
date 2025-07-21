import os, requests, json, datetime

# 从仓库 Secrets 读配置
WEBHOOK = os.getenv("WEBHOOK")
KEY     = os.getenv("WEATHER_KEY")
CITY    = os.getenv("CITY", "北京")      # 默认北京，可在 Secrets 里改

# 1. 获取天气（和风天气 3 日预报）
location = {"北京":"101010100","上海":"101020100","广州":"101280101","深圳":"101280601"}.get(CITY, "101010100")
url = f"https://devapi.qweather.com/v7/weather/3d?location={location}&key={KEY}"
r = requests.get(url, timeout=10).json()
today = r["daily"][0]
text = f"{CITY}今日天气\n" \
       f"白天：{today['textDay']}，{today['tempMax']}°C\n" \
       f"夜间：{today['textNight']}，{today['tempMin']}°C\n" \
       f"风向：{today['windDirDay']} {today['windScaleDay']}级"

# 2. 发送到飞书
payload = {"msg_type":"text","content":{"text":text}}
requests.post(WEBHOOK, json=payload, headers={"Content-Type":"application/json"})