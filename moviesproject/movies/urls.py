from rest_framework.routers import SimpleRouter 
from .views import MovieViewSet 

app_name = 'movies'

router = SimpleRouter() 
router.register('movies', MovieViewSet, basename='movie')

urlpatterns = router.urls