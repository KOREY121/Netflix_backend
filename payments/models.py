from django.db import models

from django.db import models


class Payment(models.Model):

    class Status(models.TextChoices):
        SUCCESS  = 'success',  'Success'
        FAILED   = 'failed',   'Failed'
        PENDING  = 'pending',  'Pending'
        REFUNDED = 'refunded', 'Refunded'

    class Method(models.TextChoices):
        CARD   = 'card',   'Card'
        PAYPAL = 'paypal', 'PayPal'
        MOBILE = 'mobile', 'Mobile Money'

    user           = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='payments')
    subscription   = models.ForeignKey('subscriptions.Subscription', on_delete=models.SET_NULL, null=True, blank=True)
    amount         = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=Method.choices)
    status         = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    transaction_id = models.CharField(max_length=255, blank=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return f'{self.user.email} — ${self.amount} ({self.status})'