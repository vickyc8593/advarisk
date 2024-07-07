
from django.urls import path
from .views import search_news, previous_searches, refresh_search

urlpatterns = [
    path('', search_news, name='search_news'),
    path('previous/', previous_searches, name='previous_searches'),
    path('refresh/<int:search_id>/', refresh_search, name='refresh_search'),
]
