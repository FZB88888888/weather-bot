import os, requests, json

WEBHOOK   = os.getenv("WEBHOOK")
KEY       = os.getenv("WEATHER_KEY")
CITY      = os.getenv("CITY")

# 打印实际调用的 URL 方便排查
url = f"https://devapi.qweather.com/v7/weather/3d?location={CITY}&key={KEY}"
print("Request URL:", url)

r = requests.get(url, timeout=10).json()
print("API response:", json.dumps(r, ensure_ascii=False, indent=2))

# 如果出错，直接给出原因
if "daily" not in r:
    raise RuntimeError(f"❌ API 报错：{r.get('code', 'unknown')} - {r.get('msg', 'no message')}")

today = r["daily"][0]
text = f"{CITY}今日天气\n白天：{today['textDay']} {today['tempMax']}°C\n夜间：{today['textNight']} {today['tempMin']}°C"
payload = {"msg_type":"text","content":{"text":text}}
requests.post(WEBHOOK, json=payload)
