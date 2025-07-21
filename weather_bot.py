import os, requests, json

WEBHOOK = os.getenv("WEBHOOK")
KEY     = os.getenv("WEATHER_KEY")
CITY    = os.getenv("CITY", "320506")

url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={CITY}&key={KEY}&extensions=all"
r = requests.get(url, timeout=10).json()

if r.get("status") != "1":
    raise RuntimeError(r.get("info", "高德API错误"))

today = r["forecasts"][0]["casts"][0]
text = (
    f"苏州市吴中区今日天气\n"
    f"白天：{today['dayweather']}，{today['daytemp']}°C\n"
    f"夜间：{today['nightweather']}，{today['nighttemp']}°C"
)

payload = {"msg_type": "text", "content": {"text": text}}
requests.post(WEBHOOK, json=payload)
