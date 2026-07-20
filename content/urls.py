from django.urls import path
from .views import (
    ContentListView, ContentDetailView, FeaturedContentView,
    GenreListView, SeasonListView, EpisodeListView,
)

urlpatterns = [
    path('',                                  ContentListView.as_view(),    name='content-list'),
    path('featured/',                         FeaturedContentView.as_view(),name='content-featured'),
    path('genres/',                           GenreListView.as_view(),      name='genre-list'),
    path('<int:pk>/',                         ContentDetailView.as_view(),  name='content-detail'),
    path('<int:content_id>/seasons/',         SeasonListView.as_view(),     name='season-list'),
    path('seasons/<int:season_id>/episodes/', EpisodeListView.as_view(),    name='episode-list'),
]