from django.contrib import admin
from movies.models import Movie, Rating


class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
