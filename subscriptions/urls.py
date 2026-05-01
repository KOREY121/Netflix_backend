from django.urls import path
from .views import SubscriptionListView, BillingHistoryView

urlpatterns = [
    path('',         SubscriptionListView.as_view(), name='subscription-list'),
    path('billing/', BillingHistoryView.as_view(),   name='billing-history'),
]