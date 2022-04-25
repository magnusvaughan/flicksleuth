from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from movies.models import Movie

from .serializers import MovieSerializer


class MovieListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()


class MovieRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer

    def retrieve(self, pk):
        movie = Movie.objects.order_by("?").first()
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
