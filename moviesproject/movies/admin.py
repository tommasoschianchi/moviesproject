from django.contrib import admin
from .models import Movie, StreamingChannel

admin.site.register(Movie)
admin.site.register(StreamingChannel)