import os, requests, json

WEBHOOK = os.getenv("WEBHOOK")
KEY     = os.getenv("WEATHER_KEY")
CITY    = os.getenv("CITY", "320506")

url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={CITY}&key={KEY}&extensions=all"
r = requests.get(url, timeout=10).json()

if r.get("status") != "1":
    raise RuntimeError(r.get("info", "高德API错误"))

today = r["forecasts"][0]["casts"][0]
import random, datetime

# 随机心灵鸡汤
quotes = [
    "不管今天天气如何，记得给自己一个微笑。",
    "阳光总在风雨后，愿你也如此。",
    "每一天都是新的开始，愿你心中有光。",
    "天凉加衣，心凉加糖，愿你温暖如初。",
    "把烦恼留给昨天，把希望交给明天。",
    "愿你眼里有星辰，心中有暖阳。",
    "天气在变，心情别变，保持热爱，奔赴山海。",
]

today_quote = random.choice(quotes)

text = (
    f"【机器人】苏州市吴中区今日天气\n"
    f"白天：{today['dayweather']}，{today['daytemp']}°C\n"
    f"夜间：{today['nightweather']}，{today['nighttemp']}°C\n"
    f"—— {today_quote}"
)

payload = {"msg_type": "text", "content": {"text": text}}
requests.post(WEBHOOK, json=payload)
