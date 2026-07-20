from django.db import models


from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Content(models.Model):

    class Type(models.TextChoices):
        MOVIE  = 'Movie',  'Movie'
        SERIES = 'Series', 'Series'

    class AgeRating(models.TextChoices):
        G     = 'G',     'G'
        PG    = 'PG',    'PG'
        PG13  = 'PG-13', 'PG-13'
        R     = 'R',     'R'
        TV14  = 'TV-14', 'TV-14'
        TVMA  = 'TV-MA', 'TV-MA'

    title         = models.CharField(max_length=255)
    description   = models.TextField()
    release_year  = models.PositiveSmallIntegerField()
    duration      = models.PositiveIntegerField(default=0, help_text='Minutes (movies only)')
    type          = models.CharField(max_length=10, choices=Type.choices)
    age_rating    = models.CharField(max_length=10, choices=AgeRating.choices)
    genres        = models.ManyToManyField(Genre, through='ContentGenre', related_name='content')
    thumbnail_url = models.URLField(blank=True)
    trailer_url   = models.URLField(blank=True)
    is_featured   = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'content'

    def __str__(self):
        return f'{self.title} ({self.release_year})'


class ContentGenre(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    genre   = models.ForeignKey(Genre,   on_delete=models.CASCADE)

    class Meta:
        db_table        = 'content_genres'
        unique_together = ('content', 'genre')


class Season(models.Model):
    content       = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='seasons')
    season_number = models.PositiveSmallIntegerField()
    title         = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table        = 'seasons'
        unique_together = ('content', 'season_number')

    def __str__(self):
        return f'{self.content.title} — S{self.season_number}'


class Episode(models.Model):
    season         = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='episodes')
    episode_number = models.PositiveSmallIntegerField()
    title          = models.CharField(max_length=255)
    duration       = models.PositiveIntegerField(help_text='Minutes')
    description    = models.TextField(blank=True)

    class Meta:
        db_table        = 'episodes'
        unique_together = ('season', 'episode_number')

    def __str__(self):
        return f'{self.season} E{self.episode_number}: {self.title}'