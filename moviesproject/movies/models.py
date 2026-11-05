from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
