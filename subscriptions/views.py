from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Subscription, BillingHistory
from .serializers import SubscriptionSerializer, BillingHistorySerializer


class SubscriptionListView(generics.ListAPIView):
    queryset           = Subscription.objects.filter(is_active=True)
    serializer_class   = SubscriptionSerializer
    permission_classes = [permissions.AllowAny]


class BillingHistoryView(generics.ListAPIView):
    serializer_class   = BillingHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BillingHistory.objects.filter(
            user=self.request.user
        ).select_related('subscription')