from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from movies.models import Movie

from .serializers import MovieSerializer


class MovieListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()
