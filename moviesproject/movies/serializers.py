from rest_framework import serializers
from .models import Movie, StreamingChannel

__all__ = ["MovieSerializer"]

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'subtitle', 'director', 'description', 'streaming_channel']
class StreamingChannelSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source='movie_set', many=True, read_only=True)

    class Meta:
        model = StreamingChannel
        fields = ['id', 'name', 'description', 'movies']