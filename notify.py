import requests

def notify(driver, message):
    BOT_TOKEN = ''
    CHAT_ID = '108603036'
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)
    if response.ok:
        print("✅ Повідомлення надіслано!")
    else:
        print("❌ Помилка:", response.text)
