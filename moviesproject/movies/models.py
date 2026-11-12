from django.contrib.auth import get_user_model # new
from django.db import models

USER = get_user_model() # new

__all__ = ["Movie"] # new

class StreamingChannel(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(
        USER,
        on_delete=models.PROTECT,
        default=None,
        null=True,
    ) # new


    def __str__(self):
        return self.name


class Movie(models.Model):
    owner = models.ForeignKey(
    USER,
    on_delete=models.PROTECT,
    default=None,
    null=True,
    ) # new
    title = models.CharField(max_length=250)
    subtitle = models.CharField(
    max_length=250,
    null=True,
    blank=True
    )
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    streaming_channel = models.ForeignKey(
        StreamingChannel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
     return self.title

