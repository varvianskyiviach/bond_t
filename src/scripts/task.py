from typing import Dict, List

from movies.models import Movie, Person


def fill_database_from_data(movies_data: List[Dict[str, str]]):

    for movie_data in movies_data:

        directors: List[str] = [
            Person.objects.get_or_create(name=director.strip())[0] for director in movie_data.get("Director").split(",")
        ]
        actors: List[str] = [
            Person.objects.get_or_create(name=actor.strip())[0] for actor in movie_data.get("Actors").split(",")
        ]
        print(directors, actors)
        movie, created = Movie.objects.get_or_create(
            title=movie_data.get("Title"), release_year=int(movie_data.get("Year"))
        )

        movie.directors.add(*directors)
        movie.actors.add(*actors)
        movie.save()

        if created:
            print(f"Movie '{movie.title}' was created successfully")
        else:
            print(f"Movie '{movie.title}' already exists")
