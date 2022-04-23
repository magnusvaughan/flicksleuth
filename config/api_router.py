from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from flicksleuth.users.api.views import UserViewSet
from movies.api.views import MovieListView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

app_name = "api"

urlpatterns = [path("movies", MovieListView.as_view())]

urlpatterns += router.urls
