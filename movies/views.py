from django.contrib.auth.models import User
from movies.models import Movie, Genre, Rating
from rest_framework import viewsets
from movies.serializers import UserSerializer, MovieSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
