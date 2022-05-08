from django.contrib import admin

from movies.models import Actor, Movie, MovieActor


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
    )


admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(MovieActor)
