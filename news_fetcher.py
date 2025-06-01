import requests

API_KEY = "605e8ea6186244ce5ab6b2599a548e37a22e0d7c"
NEWS_ENDPOINT = "https://cryptopanic.com/api/v1/posts/"

def get_crypto_news():
    params = {
        'auth_token': API_KEY,
        'public': 'true',
        'currencies': 'BTC,ETH',  # можно добавить любые другие токены
        'kind': 'news',
        'regions': 'en'
    }

    try:
        response = requests.get(NEWS_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()

        news_items = []
        for item in data.get("results", [])[:5]:
            title = item.get("title")
            url = item.get("url")
            published = item.get("published_at")
            news_items.append(f"📰 {title}\n🔗 {url}\n🕒 {published}\n")

        return "\n".join(news_items) if news_items else "Нет свежих новостей на текущий момент."

    except Exception as e:
        return f"❗ Ошибка при получении новостей: {e}"