import requests
import time

url = "https://tv-breakout-alerts.vercel.app/webhook"

payload = {
    "type": "CONFIRMED_CE_BUY",
    "current_symbol": "NIFTY260224C25500",
    "opposite_symbol": "NIFTY260224P25500",
    "current_chart": "https://www.tradingview.com/chart/?symbol=NSE:NIFTY260224C25500",
    "opposite_chart": "https://www.tradingview.com/chart/?symbol=NSE:NIFTY260224P25500",
    "ce_status": "RISING",
    "pe_status": "FALLING",
    "pivot_price": 120.5,
    "confirm_price": 135.2,
    "pivot_id": "PE_TO_CE_BUY",
    "confirm_time": time.strftime("%H:%M:%S"),
    "timestamp": int(time.time() * 1000)
}

response = requests.post(url, json=payload, timeout=10)

print("Status Code:", response.status_code)
print("Response:", response.text)
