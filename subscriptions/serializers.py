from rest_framework import serializers
from .models import Subscription, BillingHistory


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'plan_name', 'price', 'max_streams', 'description', 'is_active']


class BillingHistorySerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source='subscription.plan_name', read_only=True)
    price = serializers.DecimalField(
        source='subscription.price', max_digits=6, decimal_places=2, read_only=True
    )

    class Meta:
        model  = BillingHistory
        fields = ['id', 'plan_name', 'price', 'start_date', 'end_date', 'status', 'created_at']