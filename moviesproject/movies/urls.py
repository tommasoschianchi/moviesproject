from django.urls import path
from movies.views import CreateMovie, ListMovie, DetailMovie, MovieFilterList

app_name = 'movies'

urlpatterns = [
    path('create/', CreateMovie.as_view(), name='create-movie'),
    path('<int:pk>/', DetailMovie.as_view()),
    path('filter/', MovieFilterList.as_view(), name='filter-movie'),
    path('', ListMovie.as_view()),
]
