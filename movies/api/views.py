from datetime import date

import requests
from django.conf import settings
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie

from .serializers import MovieSerializer


class MovieListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        query = self.request.query_params.get("query")
        url = "https://movie-database-alternative.p.rapidapi.com/"
        querystring = {"s": query, "r": "json", "page": "1"}
        headers = {
            "X-RapidAPI-Host": settings.MOVIE_API["XRapidAPIHost"],
            "X-RapidAPI-Key": settings.MOVIE_API["XRapidAPIKey"],
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response(response.text)


class MovieRetrieveView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = MovieSerializer

    def retrieve(self, pk):
        today = date.today()
        movie = Movie.objects.get(
            date__year=today.year, date__month=today.month, date__day=today.day
        )
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
