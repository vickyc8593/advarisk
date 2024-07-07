import requests
from .models import SearchResult

def fetch_news_articles(keyword, from_date=None):
    NEWS_API_KEY = '3278c0bf0b5541d1aa12cb5bc563de86'
    NEWS_API_URL = 'https://newsapi.org/v2/everything'

    params = {
        'q': keyword,
        'apiKey': NEWS_API_KEY,
    }

    if from_date:
        params['from'] = from_date.date().isoformat()

    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise exception for non-200 response codes
        data = response.json()

        if not data or 'articles' not in data:
            return []  # Return empty list if data is None or 'articles' key is missing

        articles = data.get('articles', [])
        if not articles:
            return []

        return articles

    except requests.exceptions.RequestException as e:
        # Handle API request error (e.g., network issues, API service down)
        print(f"Error fetching news articles: {e}")
        return []  # Return empty list if error occurs
