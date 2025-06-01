import os
import asyncio
import openai
import requests
import pandas as pd
from telegram import Bot
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=TOKEN)
scheduler = AsyncIOScheduler()

excel_file = "trades.xlsx"
if not os.path.exists(excel_file):
df = pd.DataFrame(columns=["Дата", "Сделка", "Тип", "Монета", "Цена входа", "SL", "TP", "Комментарий"])
df.to_excel(excel_file, index=False)

# ========== Новости ==========
async def send_crypto_news():
news = "📰 Крипто-новости за сегодня:\n\n• BTC стабилен\n• ETF одобрен в США\n• Объемы торгов растут."
await bot.send_message(chat_id=CHAT_ID, text=news)

# ========== Генерация сделок ==========
async def send_trade(time_tag):
deals = {
"12:00": [
{"coin": "BTCUSDT", "type": "Long", "entry": 68500, "sl": 67400, "tp": 69900},
{"coin": "LTCUSDT", "type": "Short", "entry": 86.50, "sl": 88.00, "tp": 82.00}
],
"18:00": [
{"coin": "ETHUSDT", "type": "Long", "entry": 3740, "sl": 3650, "tp": 3880},
{"coin": "NEARUSDT", "type": "Short", "entry": 7.45, "sl": 7.75, "tp": 6.80}
]
}

msg = f"💹 Сделки на {time_tag}:\n"
for d in deals[time_tag]:
msg += f"\n📈 {d['coin']} ({d['type']})\n• Вход: {d['entry']}\n• SL: {d['sl']}\n• TP: {d['tp']}\n"

# Запись в Excel
df = pd.read_excel(excel_file)
df.loc[len(df)] = [
datetime.now().strftime("%Y-%m-%d %H:%M"),
"⏰ " + time_tag,
d['type'],
d['coin'],
d['entry'],
d['sl'],
d['tp'],
"Автоматическая сделка"
]
df.to_excel(excel_file, index=False)

await bot.send_message(chat_id=CHAT_ID, text=msg)

# ========== Почасовой отчёт ==========
async def hourly_report():
df = pd.read_excel(excel_file)
latest = df.tail(3)
text = "🕐 Почасовой отчёт по последним сделкам:\n"
for _, row in latest.iterrows():
text += f"\n• {row['Монета']} ({row['Тип']}) — Вход {row['Цена входа']}, SL {row['SL']}, TP {row['TP']}"
await bot.send_message(chat_id=CHAT_ID, text=text)

# ========== Критические уведомления ==========
async def check_critical_condition():
critical_text = "⚠️ Внимание! Сделка по BTCUSDT близка к ликвидации. Перепроверьте Stop-Loss!"
await bot.send_message(chat_id=CHAT_ID, text=critical_text)

# ========== Планировщик ==========
def setup_scheduler():
scheduler.add_job(send_crypto_news, 'cron', hour=6, minute=0)
scheduler.add_job(send_trade, 'cron', hour=12, minute=0, args=["12:00"])
scheduler.add_job(send_trade, 'cron', hour=18, minute=0, args=["18:00"])
scheduler.add_job(hourly_report, 'cron', minute=0)
scheduler.add_job(check_critical_condition, 'interval', minutes=10)
scheduler.start()

# ========== Запуск ==========
if __name__ == "__main__":
setup_scheduler()
print("✅ Бот запущен из облака.")
asyncio.get_event_loop().run_forever()
