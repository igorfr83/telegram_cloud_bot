from pyrogram import Client, filters
from news_fetcher import get_crypto_news

# Конфигурация
api_id = 123456 # можно оставить пустым, если не используешь MTProto
api_hash = "your_api_hash" # тоже не нужен для обычного бота
bot_token = "7910658659:AAG-qyMEV5ZiDmlxhhxT5oGimfIKfzEThYY"
chat_id = 336663757

# Инициализация бота
app = Client("crypto_bot", bot_token=bot_token)

# Команда /start
@app.on_message(filters.command("start"))
def start(client, message):
message.reply("👋 Привет! Я бот по криптовалюте. Используй /news, чтобы получить свежие новости.")

# Команда /news
@app.on_message(filters.command("news"))
def send_news(client, message):
news = get_crypto_news()
client.send_message(chat_id=message.chat.id, text=news)

# Запуск бота
app.run()
