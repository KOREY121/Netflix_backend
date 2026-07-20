from django.urls import path
from .views import (
    ReviewListCreateView, ReviewDetailView,
    MyListView, ToggleMyListView, RecommendationListView,
)

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('my-list/', MyListView.as_view(), name='my-list'),
    path('my-list/toggle/', ToggleMyListView.as_view(), name='my-list-toggle'),
    path('recommendations/', RecommendationListView.as_view(), name='recommendations'),
]