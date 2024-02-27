from django.db import models


class Person(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):

    directors = models.ManyToManyField(Person, related_name="directed_movies")
    actors = models.ManyToManyField(Person, related_name="acted_movies")

    tittle = models.CharField(max_length=255, unique=True)
    release_year = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.tittle
