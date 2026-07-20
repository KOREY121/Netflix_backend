from rest_framework import serializers
from .models import Content, Genre, Season, Episode


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genre
        fields = ['id', 'name']


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Episode
        fields = ['id', 'episode_number', 'title', 'duration', 'description']


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model  = Season
        fields = ['id', 'season_number', 'title', 'episodes']


class ContentListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model  = Content
        fields = ['id', 'title', 'type', 'release_year', 'duration',
                  'age_rating', 'thumbnail_url', 'genres', 'is_featured']


class ContentDetailSerializer(serializers.ModelSerializer):
    genres  = GenreSerializer(many=True, read_only=True)
    seasons = SeasonSerializer(many=True, read_only=True)

    class Meta:
        model  = Content
        fields = ['id', 'title', 'description', 'type', 'release_year',
                  'duration', 'age_rating', 'thumbnail_url', 'trailer_url',
                  'is_featured', 'genres', 'seasons', 'created_at']