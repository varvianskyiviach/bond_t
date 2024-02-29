from django.contrib import admin

from movies.models import Movie, Person


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    def get_directors(self, obj):
        return ", ".join([director.name for director in obj.directors.all()])

    def get_actors(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])

    list_display = ["id", "title", "get_directors", "get_actors", "release_year"]
    search_fields = ["title", "directors__name", "actors__name", "release_year"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = ["id", "name"]
