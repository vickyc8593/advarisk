# news/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError
from .models import SearchResult
from .utils import fetch_news_articles

def search_news(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        articles = fetch_news_articles(keyword)

        if articles is None:  # Check if articles is None (no results or error)
            return HttpResponseServerError("No articles found or error fetching news articles.")

        if not articles:  # Check if articles is empty (no results found)
            return render(request, 'news/no_results.html', {'keyword': keyword})

        # Sort articles by publishedAt (assuming it's already sorted)
        articles.sort(key=lambda x: x.get('publishedAt', ''), reverse=True)

        return render(request, 'news/results.html', {'articles': articles})

    return render(request, 'news/search.html')

def previous_searches(request):
    searches = SearchResult.objects.all().order_by('-created_at')
    return render(request, 'news/previous_searches.html', {'searches': searches})

def refresh_search(request, search_id):
    search = get_object_or_404(SearchResult, id=search_id)
    keyword = search.keyword
    articles = fetch_news_articles(keyword)

    if not articles:  # Check if articles is empty or None
        return render(request, 'news/no_results.html', {'keyword': keyword})

    SearchResult.objects.filter(keyword=keyword).delete()

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

    return redirect('previous_searches')
