from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    profile     = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='reviews')
    content     = models.ForeignKey('content.Content',  on_delete=models.CASCADE, related_name='reviews')
    rating      = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table        = 'reviews'
        unique_together = ('profile', 'content')

    def __str__(self):
        return f'{self.profile.name} → {self.content.title} ({self.rating}★)'


class MyList(models.Model):
    profile  = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='my_list')
    content  = models.ForeignKey('content.Content',  on_delete=models.CASCADE, related_name='in_my_lists')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table        = 'my_list'
        unique_together = ('profile', 'content')

    def __str__(self):
        return f'{self.profile.name} saved {self.content.title}'


class Recommendation(models.Model):
    profile      = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='recommendations')
    content      = models.ForeignKey('content.Content',  on_delete=models.CASCADE, related_name='recommended_to')
    score        = models.FloatField(help_text='0.0 – 1.0 relevance score')
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table        = 'recommendations'
        unique_together = ('profile', 'content')

    def __str__(self):
        return f'{self.profile.name} ← {self.content.title} ({self.score:.2f})'