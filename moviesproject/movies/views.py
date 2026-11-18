from rest_framework import viewsets, permissions
from .models import Movie, StreamingChannel
from .serializers import MovieSerializer, StreamingChannelSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiTypes        

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

BAD_REQUEST_RESPONSE= OpenApiExample(
    'Bad Request',
    value={"message": "Bad Request"},
    status_codes=400,     
)   
@extend_schema(
    responses={
        200: MovieSerializer,
        400: OpenApiTypes.OBJECT,
    },
    examples=[BAD_REQUEST_RESPONSE]
)
class MovieViewSet(viewsets.ModelViewSet):
    model: Movie
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()