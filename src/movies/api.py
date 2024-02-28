from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer
from shared.django.pagination import CustomPagination


class MovieAPISet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
