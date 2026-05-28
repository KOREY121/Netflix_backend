from django.urls import path
from .views import PaymentHistoryView

urlpatterns = [
    path('', PaymentHistoryView.as_view(), name='payment-history'),
]