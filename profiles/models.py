from django.db import models

class Profile(models.Model):

    class MaturityLevel(models.TextChoices):
        KIDS = 'Kids', 'Kids'
        TEEN = 'Teen', 'Teen'
        ADULT = 'Adult', 'Adult'

    user =models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='profiles'
    )
    name = models.CharField(max_length=30)
    avatar_url = models.URLField(blank=True)
    maturity_level = models.CharField(
        max_length=10, choices = MaturityLevel.choices,
        default= MaturityLevel.ADULT,
    )
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return f'{self.user.email} → {self.name}'