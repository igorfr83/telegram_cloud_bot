from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_message():
    await bot.send_message(chat_id=CHAT_ID, text="Привет! Бот работает на Render ☁️")

if name == "__main__":
    asyncio.run(send_message())