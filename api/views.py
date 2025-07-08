from rest_framework import viewsets # <--- Import viewsets
from movies.models import Movie
from .serializers import MovieSerializer

# Define MovieViewSet that inherits from ModelViewSet
class MovieViewSet(viewsets.ModelViewSet): # <--- Define this class
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer