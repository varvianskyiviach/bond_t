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
    path("movies/", views.MovieListView.as_view(), name="movie_list"),
    path("movies/<int:pk>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("movies/create/", views.MovieCreateView.as_view(), name="movie_create"),
    path("movies/<int:pk>/update/", views.MovieUpdateView.as_view(), name="movie_update"),
    path("movies/<int:pk>/delete/", views.MovieDeleteView.as_view(), name="movie_delete"),
]
