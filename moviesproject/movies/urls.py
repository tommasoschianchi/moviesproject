from rest_framework.routers import SimpleRouter 
from .views import MovieViewSet, StreamingChannelViewSet

app_name = 'movies'

router = SimpleRouter() 
router.register('movies', MovieViewSet, basename='movie')
router.register('streaming-channels', StreamingChannelViewSet, basename='streamingchannel')

urlpatterns = router.urls