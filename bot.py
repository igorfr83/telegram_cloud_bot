import os
import asyncio
from pyrogram import Client, filters
from news_fetcher import get_crypto_news
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")

app = Client("crypto_bot", bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Привет! Я бот по криптовалюте. Используй команду /news")

@app.on_message(filters.command("news"))
async def news(client, message):
    news = get_crypto_news()
    await client.send_message(chat_id=message.chat.id, text=news)

if __name__ == "__main__":
    app.run()
