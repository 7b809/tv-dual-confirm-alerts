import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BREAKOUT_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text, max_retries=3):

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Telegram credentials missing.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(url, json=payload, timeout=10)
            print(f"📤 Telegram API response: {response.status_code} - {response.text}")
            if response.status_code == 200:
                return True
            else:
                print(f"⚠ Attempt {attempt}: Telegram API error {response.status_code} - {response.text}")

        except requests.exceptions.Timeout:
            print(f"⏳ Attempt {attempt}: Timeout error")

        except requests.exceptions.ConnectionError:
            print(f"🌐 Attempt {attempt}: Connection error")

        except Exception as e:
            print(f"🔥 Attempt {attempt}: Unexpected error - {str(e)}")

        # Wait before retrying
        if attempt < max_retries:
            time.sleep(2)

    print("❌ Failed to send Telegram message after retries.")
    return False
