import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("7910658659:AAG-qyMEV5ZiDmlxhhxT5oGimfIKfzEThYY")
CHAT_ID = os.getenv("336663757")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="✅ Бот работает из облака!")