from django.db import models
from django.contrib.auth.models import User


ratings = (
    (0, "Awful"),
    (1, "Didn't Like"),
    (2, "OK"),
    (3, "Liked"),
    (4, "Amazing")
)


class Movie(models.Model):
    title = models.CharField(max_length=300)
    original_title = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    runtime = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    imdb = models.URLField()
    plot = models.TextField()
    cover = models.CharField(max_length=40)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    genres = models.ManyToManyField('Genre')
    ratings = models.ManyToManyField(User, through='Rating')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Genre(models.Model):
    genre = models.CharField(max_length=32)

    def __unicode__(self):
        return self.genre


class Rating(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey(Movie)
    rating = models.PositiveSmallIntegerField(choices=ratings, default=2)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __unicode__(self):
        return "{0} - {1}: {2}".format(self.user, self.movie, self.rating)
