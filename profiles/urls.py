from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView, SetDefaultProfileView

urlpatterns = [
    path('', ProfileListCreateView.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<int:pk>/set-default/', SetDefaultProfileView.as_view(), name='profile-set-default'),
]