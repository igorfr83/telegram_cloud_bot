import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()  # Подгрузка переменных из .env (локально, если нужно)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Бот работает из облака!")
