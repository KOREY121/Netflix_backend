from rest_framework import serializers
from .models import WatchHistory, StreamingSession, Download, SearchHistory, Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Device
        fields = ['id', 'device_name', 'device_type', 'last_active_at']


class WatchHistorySerializer(serializers.ModelSerializer):
    content_title = serializers.CharField(source='content.title', read_only=True)
    episode_title = serializers.CharField(source='episode.title', read_only=True)

    class Meta:
        model  = WatchHistory
        fields = ['id', 'profile', 'content', 'content_title',
                  'episode', 'episode_title', 'progress', 'watched_at']
        read_only_fields = ['id', 'watched_at']


class StreamingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = StreamingSession
        fields = ['id', 'profile', 'device', 'content', 'episode',
                  'start_time', 'end_time', 'status']
        read_only_fields = ['id', 'start_time']

    def validate(self, attrs):
        # Enforce max_streams per subscription plan
        profile      = attrs['profile']
        subscription = profile.user.subscription
        if subscription:
            active = StreamingSession.objects.filter(
                profile__user=profile.user,
                status=StreamingSession.Status.ACTIVE
            ).count()
            if active >= subscription.max_streams:
                raise serializers.ValidationError(
                    f'Your {subscription.plan_name} plan allows '
                    f'{subscription.max_streams} stream(s) at once.'
                )
        return attrs


class DownloadSerializer(serializers.ModelSerializer):
    content_title = serializers.CharField(source='content.title', read_only=True)

    class Meta:
        model  = Download
        fields = ['id', 'profile', 'content', 'content_title',
                  'episode', 'downloaded_at', 'expires_at']
        read_only_fields = ['id', 'downloaded_at']


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = SearchHistory
        fields = ['id', 'query_text', 'searched_at']
        read_only_fields = ['id', 'searched_at']