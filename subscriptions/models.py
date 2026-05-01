from django.db import models

from django.db import models


class Subscription(models.Model):

    class Plan(models.TextChoices):
        BASIC    = 'Basic',    'Basic'
        STANDARD = 'Standard', 'Standard'
        PREMIUM  = 'Premium',  'Premium'

    plan_name   = models.CharField(max_length=20, choices=Plan.choices, unique=True)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    max_streams = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        db_table = 'subscriptions'

    def __str__(self):
        return f'{self.plan_name} — ${self.price}/mo'


class BillingHistory(models.Model):

    class Status(models.TextChoices):
        ACTIVE   = 'active',   'Active'
        EXPIRED  = 'expired',  'Expired'
        CANCELED = 'canceled', 'Canceled'

    user         = models.ForeignKey('users.User',       on_delete=models.CASCADE, related_name='billing_history')
    subscription = models.ForeignKey(Subscription,       on_delete=models.CASCADE, related_name='billing_records')
    start_date   = models.DateField()
    end_date     = models.DateField()
    status       = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'billing_history'

    def __str__(self):
        return f'{self.user.email} — {self.subscription.plan_name}'