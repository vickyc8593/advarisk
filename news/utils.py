import requests
from .models import SearchResult
from datetime import datetime, timedelta
from django.core.cache import cache

def fetch_news_articles(keyword):
    NEWS_API_KEY = '3278c0bf0b5541d1aa12cb5bc563de86'
    NEWS_API_URL = 'https://newsapi.org/v2/everything'

    params = {
        'q': keyword,
        'apiKey': NEWS_API_KEY,
    }

    # Check if cached data exists
    cache_key = f'news_articles_{keyword}'
    cached_data = cache.get(cache_key)

    if cached_data:
        return cached_data

    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Raise exception for non-200 response codes
        data = response.json()

        if not data or 'articles' not in data:
            return []  # Return empty list if data is None or 'articles' key is missing

        articles = data.get('articles', [])
        if not articles:
            return []

        # Filter articles published after the last cached timestamp
        if cached_data and 'last_fetched' in cached_data:
            last_fetched = datetime.strptime(cached_data['last_fetched'], '%Y-%m-%dT%H:%M:%SZ')
            articles = [article for article in articles if datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ') > last_fetched]

        # Cache the new data
        cache.set(cache_key, {'articles': articles, 'last_fetched': datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')}, timeout=60 * 15)  # Cache for 15 minutes

        return articles

    except requests.exceptions.RequestException as e:
        # Handle API request error (e.g., network issues, API service down)
        print(f"Error fetching news articles: {e}")
        return []  # Return empty list if error occurs
