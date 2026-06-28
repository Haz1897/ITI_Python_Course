from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "categories"


class Cast(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "casts"


class MediaBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name="%(class)s_set", blank=True)
    casts = models.ManyToManyField(Cast, related_name="%(class)s_set", blank=True)
    poster_image = models.ImageField(upload_to="posters/", null=True, blank=True)

    class Meta:
        abstract = True


class Movie(MediaBase):
    duration_minutes = models.PositiveIntegerField(help_text="Runtime in minutes")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "movies"


class Series(MediaBase):
    seasons = models.PositiveIntegerField(default=1)
    episodes_per_season = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        db_table = "series"