import os
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from news_fetcher import get_crypto_news

# Загружаем переменные окружения
load_dotenv()

# Получаем токены из окружения
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Инициализируем бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("👋 Привет! Я бот по криптовалюте. Используй команду /news, чтобы получить свежие новости.")

# Команда /news
@dp.message_handler(commands=['news'])
async def news_handler(message: types.Message):
    news = get_crypto_news()
    await message.answer(news)

# Запуск
if__name == "__main__":
    executor.start_polling(dp)
