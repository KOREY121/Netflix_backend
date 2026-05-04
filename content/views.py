from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Content, Genre, Season, Episode
from .serializers import (ContentListSerializer, ContentDetailSerializer,GenreSerializer, SeasonSerializer, EpisodeSerializer,)


class ContentListView(generics.ListAPIView):
    serializer_class   = ContentListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields      = ['title', 'description']
    ordering_fields    = ['release_year', 'created_at']
    filterset_fields   = ['type', 'age_rating', 'is_featured']

    def get_queryset(self):
        return Content.objects.prefetch_related('genres').all()


class ContentDetailView(generics.RetrieveAPIView):
    serializer_class   = ContentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Content.objects.prefetch_related('genres', 'seasons__episodes')


class FeaturedContentView(generics.ListAPIView):
    serializer_class   = ContentListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Content.objects.filter(is_featured=True).prefetch_related('genres')


class GenreListView(generics.ListAPIView):
    queryset           = Genre.objects.all()
    serializer_class   = GenreSerializer
    permission_classes = [permissions.AllowAny]


class SeasonListView(generics.ListAPIView):
    serializer_class   = SeasonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Season.objects.filter(
            content_id=self.kwargs['content_id']
        ).prefetch_related('episodes')


class EpisodeListView(generics.ListAPIView):
    serializer_class   = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Episode.objects.filter(season_id=self.kwargs['season_id'])