import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

# , CommandError

# from movies.models import Actor, Movie


class Command(BaseCommand):
    help = "Adds movie data to the db"

    def add_arguments(self, parser):
        parser.add_argument("movie_id", type=str)

    def handle(self, *args, **options):
        url = f"https://www.imdb.com/title/tt{options['movie_id']}/fullcredits"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.select("h3 > a")[0].text
        print(title)
        year = soup.select(".nobr")[0].text.replace("(", "").replace(")", "")
        print(year)
        cast = soup.select("td.primary_photo + td > a")
        for actor in cast:
            print(actor.text)
