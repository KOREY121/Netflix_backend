from django.urls import path
from .views import (
    WatchHistoryListView, UpdateWatchHistoryView,
    StartSessionView, EndSessionView,
    DownloadListCreateView, DeviceListView, SearchHistoryView,
)

urlpatterns = [
    path('history/', WatchHistoryListView.as_view(), name='watch-history'),
    path('history/update/', UpdateWatchHistoryView.as_view(), name='watch-history-update'),
    path('sessions/start/', StartSessionView.as_view(), name='session-start'),
    path('sessions/<int:pk>/end/', EndSessionView.as_view(), name='session-end'),
    path('downloads/', DownloadListCreateView.as_view(), name='downloads'),
    path('devices/', DeviceListView.as_view(), name='devices'),
    path('search-history/', SearchHistoryView.as_view(), name='search-history'),
]