from django.db import models
from django.utils.timezone import now


class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    actors = models.ManyToManyField(Actor, through="MovieActor")
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} - {self.date:%d-%m-%Y}"


class MovieActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    credit_position = models.IntegerField(blank=True, null=True)
