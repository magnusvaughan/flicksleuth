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
        url = f"https://www.imdb.com/title/tt{options['movie_id']}/fullcredits"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.select("h3 > a")[0].text
        # year = soup.select(".nobr")[0].text.replace("(", "").replace(")", "")
        cast = soup.select("td.primary_photo + td > a")
        new_movie = Movie.objects.get_or_create(title=title)[0]
        for actor in cast:
            new_actor = Actor.objects.get_or_create(name=actor.text)[0]
            new_movie.actors.add(new_actor)
