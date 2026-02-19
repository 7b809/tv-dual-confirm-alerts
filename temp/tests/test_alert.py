import requests
import time

url = "http://127.0.0.1:5000/webhook"

payload = {
    "type": "CONFIRMED_CE_BUY",
    "ticker": "NIFTY260224C25500",
    "pivot_price": 120.5,
    "confirm_price": 135.2,
    "confirm_time": time.strftime("%H:%M:%S"),
    "timestamp": int(time.time()),
    "chart": "https://www.tradingview.com/chart/"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.text)
