
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

class ListMovie(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DetailMovie(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CreateMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieFilterList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        text=self.request.GET.get('filter', "")
        return Movie.objects.filter(title__contains=text).all()