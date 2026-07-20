from django.shortcuts import render

from django.utils import timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import WatchHistory,StreamingSession,SearchHistory,Device,Download
from .serializers import ( WatchHistorySerializer, StreamingSessionSerializer, DownloadSerializer, SearchHistorySerializer, DeviceSerializer)


class WatchHistoryListView(generics.ListAPIView):
    serializer_class   = WatchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        qs = WatchHistory.objects.filter(profile__user=self.request.user)
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs


class UpdateWatchHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        profile_id = request.data.get('profile')
        content_id = request.data.get('content')
        episode_id = request.data.get('episode')
        progress   = request.data.get('progress', 0)

        lookup = {'profile_id': profile_id}
        if episode_id:
            lookup['episode_id'] = episode_id
        elif content_id:
            lookup['content_id'] = content_id
        else:
            return Response({'detail': 'content or episode required.'}, status=400)

        obj, created = WatchHistory.objects.update_or_create(
            **lookup,
            defaults={'content_id': content_id, 'episode_id': episode_id, 'progress': progress}
        )
        return Response(WatchHistorySerializer(obj).data)


class StartSessionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = StreamingSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EndSessionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            session = StreamingSession.objects.get(
                pk=pk, profile__user=request.user, status='active'
            )
        except StreamingSession.DoesNotExist:
            return Response({'detail': 'Session not found.'}, status=404)
        session.status   = 'ended'
        session.end_time = timezone.now()
        session.save()
        return Response(StreamingSessionSerializer(session).data)


class DownloadListCreateView(generics.ListCreateAPIView):
    serializer_class   = DownloadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Download.objects.filter(profile__user=self.request.user)


class DeviceListView(generics.ListCreateAPIView):
    serializer_class   = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SearchHistoryView(generics.ListCreateAPIView):
    serializer_class   = SearchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile')
        qs = SearchHistory.objects.filter(profile__user=self.request.user)
        if profile_id:
            qs = qs.filter(profile_id=profile_id)
        return qs.order_by('-searched_at')[:50]