import requests
import time

url = "https://tv-breakout-alerts.vercel.app/webhook"

def send_test(payload):
    response = requests.post(url, json=payload, timeout=10)
    print("Sent:", payload["type"], "| Symbol:", payload["current_symbol"])
    print("Status Code:", response.status_code)
    print("Response:", response.text)
    print("-" * 50)


# 1️⃣ CE RISING (NIFTY)
ce_rising_payload = {
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

# 2️⃣ PE RISING (NIFTY)
pe_rising_payload = {
    "type": "CONFIRMED_PE_BUY",
    "current_symbol": "NIFTY260224P25500",
    "opposite_symbol": "NIFTY260224C25500",
    "current_chart": "https://www.tradingview.com/chart/?symbol=NSE:NIFTY260224P25500",
    "opposite_chart": "https://www.tradingview.com/chart/?symbol=NSE:NIFTY260224C25500",
    "ce_status": "FALLING",
    "pe_status": "RISING",
    "pivot_price": 98.2,
    "confirm_price": 110.4,
    "pivot_id": "CE_TO_PE_BUY",
    "confirm_time": time.strftime("%H:%M:%S"),
    "timestamp": int(time.time() * 1000)
}

# 3️⃣ CE RISING (SENSEX)
sensex_payload = {
    "type": "CONFIRMED_CE_BUY",
    "current_symbol": "SENSEX260224C75000",
    "opposite_symbol": "SENSEX260224P75000",
    "current_chart": "https://www.tradingview.com/chart/?symbol=BSE:SENSEX260224C75000",
    "opposite_chart": "https://www.tradingview.com/chart/?symbol=BSE:SENSEX260224P75000",
    "ce_status": "RISING",
    "pe_status": "FALLING",
    "pivot_price": 210.7,
    "confirm_price": 235.3,
    "pivot_id": "PE_TO_CE_BUY",
    "confirm_time": time.strftime("%H:%M:%S"),
    "timestamp": int(time.time() * 1000)
}


# Send All Tests
send_test(ce_rising_payload)
time.sleep(1)

send_test(pe_rising_payload)
time.sleep(1)

send_test(sensex_payload)
