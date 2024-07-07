from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError
from datetime import datetime
import requests
from .models import SearchResult
from .utils import fetch_news_articles

def search_news(request):
    if 'q' in request.GET:
        keyword = request.GET['q']
        articles = fetch_news_articles(keyword)

        if articles is None:
            return HttpResponseServerError("No articles found or error fetching news articles.")

        if not articles:
            return render(request, 'news/no_results.html', {'keyword': keyword})

        return render(request, 'news/results.html', {'articles': articles})

    return render(request, 'news/search.html')

def previous_searches(request):
    searches = SearchResult.objects.all().order_by('-created_at')
    return render(request, 'news/previous_searches.html', {'searches': searches})

def refresh_search(request, search_id):
    search = get_object_or_404(SearchResult, id=search_id)
    keyword = search.keyword

    # Retrieve the latest published_at date from existing search results
    latest_published_at = SearchResult.objects.filter(keyword=keyword).order_by('-published_at').first()
    if latest_published_at:
        latest_published_at = latest_published_at.published_at

    # Fetch new articles published after the latest_published_at date
    articles = fetch_news_articles(keyword, from_date=latest_published_at)

    if not articles:
        return render(request, 'news/no_results.html', {'keyword': keyword})

    # Delete existing search results for this keyword
    SearchResult.objects.filter(keyword=keyword).delete()

    # Save new search results to the database
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
