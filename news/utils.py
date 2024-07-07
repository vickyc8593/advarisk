# news/utils.py

import requests
from .models import SearchResult

def fetch_news_articles(keyword):
    NEWS_API_KEY = '3278c0bf0b5541d1aa12cb5bc563de86'
    NEWS_API_URL = 'https://newsapi.org/v2/everything'

    params = {
        'q': keyword,
        'apiKey': NEWS_API_KEY,
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if not data or 'articles' not in data:
            return []

        articles = data.get('articles', [])
        if not articles:
            return []

        for article in articles:
            title = article.get('title', '')
            description = article.get('description', '')[:255]
            url = article.get('url', '')
            published_at = article.get('publishedAt', '')

            SearchResult.objects.create(
                keyword=keyword,
                title=title,
                description=description,
                url=url,
                published_at=published_at,
            )

        return articles

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news articles: {e}")
        return []
