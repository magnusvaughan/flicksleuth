from django.contrib import admin

from movies.models import Actor, Movie, MovieActor

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MovieActor)
