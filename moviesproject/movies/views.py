from rest_framework import viewsets, permissions
from .models import Movie, StreamingChannel
from .serializers import MovieSerializer, StreamingChannelSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # new
    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user) 
        # new

class StreamingChannelViewSet(viewsets.ModelViewSet):
    queryset = StreamingChannel.objects.all()
    serializer_class = StreamingChannelSerializer
    permission_classes = (IsAdminOrReadOnly,)
