from django_filters import rest_framework as filters

from movies.models import Movie


class MovieFilter(filters.FilterSet):
    directors = filters.CharFilter(field_name="directors__name", lookup_expr="icontains")
    actors = filters.CharFilter(field_name="actors__name", lookup_expr="icontains")
    release_year = filters.RangeFilter()

    class Meta:
        model = Movie
        fields = [
            "directors",
            "actors",
            "release_year",
        ]
