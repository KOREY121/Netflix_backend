from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenBlacklistView
)
from .views import RegisterView, MeView, ChangePasswordView

urlpatterns =[
    path('register/', RegisterView.as_view(), name='auth-register'),
     path('login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='auth-token-refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='auth-logout'),
    path('me/', MeView.as_view(), name='user-me'),
    path('me/change-password/', ChangePasswordView.as_view(), name='change-password'),


]