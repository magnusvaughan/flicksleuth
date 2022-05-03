import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from movies.models import Actor, Movie

# , CommandError


class Command(BaseCommand):
    help = "Adds movie data to the db"

    def add_arguments(self, parser):
        parser.add_argument("movie_id", type=str)

    def handle(self, *args, **options):
        max_actors_per_movie = 10
        url = f"https://www.imdb.com/title/tt{options['movie_id']}/fullcredits"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.select("h3 > a")[0].text
        year = (
            soup.select(".nobr")[0]
            .text.replace("(", "")
            .replace(")", "")
            .lstrip()
            .rstrip()
        )
        cast = soup.select("td.primary_photo + td > a")
        new_movie = Movie.objects.get_or_create(title=title, year=year)[0]
        current_cast_index = 0
        for actor in cast:
            if current_cast_index < max_actors_per_movie:
                new_actor = Actor.objects.get_or_create(name=actor.text.strip("\n"))[0]
                new_movie.actors.add(new_actor)
                current_cast_index + 1
