from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer


class PaymentHistoryView(generics.ListAPIView):
    serializer_class   = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(
            user=self.request.user
        ).select_related('subscription')