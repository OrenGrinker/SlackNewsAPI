import requests
from config import NEWSAPI_KEY

def fetch_news():
    """Fetch top news from Israel using the NewsAPI."""
    url = f"https://newsapi.org/v2/top-headlines?country=il&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        raise Exception(f"Failed to fetch news, status code: {response.status_code}")
