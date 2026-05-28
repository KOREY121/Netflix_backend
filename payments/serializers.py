from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    subscription_plan = serializers.CharField(source='subscription.plan_name', read_only=True)

    class Meta:
        model  = Payment
        fields = ['id', 'subscription_plan', 'amount', 'payment_method',
                  'status', 'transaction_id', 'created_at']
        read_only_fields = ['id', 'status', 'transaction_id', 'created_at']