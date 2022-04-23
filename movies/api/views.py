from rest_framework.generics import ListAPIView

from movies.models import Movie

from .serializers import MovieSerializer


class MovieListView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()
