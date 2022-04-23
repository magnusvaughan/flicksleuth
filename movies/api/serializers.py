from rest_framework.serializers import ModelSerializer, RelatedField

from movies.models import Movie


class ActorListingField(RelatedField):
    def to_representation(self, value):
        return value.name


class MovieSerializer(ModelSerializer):

    actors = ActorListingField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("title", "actors")
