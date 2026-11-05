from django.urls import path
from movies.views import ListMovie, DetailMovie

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/', DetailMovie.as_view()),
    path('', ListMovie.as_view()),
    ]
