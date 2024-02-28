from typing import Any, Dict, List, Union

from rest_framework import serializers

from movies.models import Movie, Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    directors = PersonSerializer(many=True)
    actors = PersonSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data: Dict[str, Any]):
        directors_data: List[Dict[str, Any]] = validated_data.pop("directors", [])
        actors_data: List[Dict[str, Any]] = validated_data.pop("actors", [])

        title: str = validated_data.get("title")
        release_year: int = validated_data.get("release_year")

        movie, created = Movie.objects.get_or_create(title=title, defaults={"release_year": release_year})

        if created:
            for director_data in directors_data:
                director, _ = Person.objects.get_or_create(**director_data)
                movie.directors.add(director)

            for actor_data in actors_data:
                actor, _ = Person.objects.get_or_create(**actor_data)
                movie.actors.add(actor)

        return movie

    def update(self, instance, validated_data: Dict[str, Any]):

        instance.title = validated_data.get("title", instance.title)
        instance.release_year = validated_data.get("release_year", instance.release_year)

        directors_data: Union[List[Dict], None] = validated_data.get("directors")
        if directors_data:
            instance.directors.clear()
            for director_data in directors_data:
                director, _ = Person.objects.get_or_create(**director_data)
                instance.directors.add(director)

        actors_data: Union[List[Dict], None] = validated_data.get("actors")
        if actors_data:
            instance.actors.clear()
            for actor_data in actors_data:
                actor, _ = Person.objects.get_or_create(**actor_data)
                instance.actors.add(actor)

        instance.save()
        return instance
