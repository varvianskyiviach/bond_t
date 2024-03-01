from django.urls import include, path
from rest_framework.routers import DefaultRouter

from movies import views
from movies.api import MovieAPISet

router = DefaultRouter()
router.register(r"movies", MovieAPISet, basename="movies")
urlpatterns = [
    path("api/v1/", include(router.urls)),
]


urlpatterns += [
    path("movies/", views.movies_page, name="movie_list"),
    path("movies/<int:pk>/", views.movie_detail_page, name="movie_detail"),
    path("movies/create/", views.create, name="movie_create"),
    path("movies/<int:pk>/update/", views.update, name="movie_update"),
    path("movies/<int:pk>/delete/", views.delete, name="movie_delete"),
]
