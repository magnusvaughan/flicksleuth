from django.contrib import admin

from movies.models import Actor, Movie

admin.site.register(Movie)
admin.site.register(Actor)
