from django.contrib.auth.models import User
from movies.models import Movie, Rating, Genre
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
