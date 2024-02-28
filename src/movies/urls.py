from django.urls import include, path
from rest_framework.routers import DefaultRouter

from movies.api import MovieAPISet

router = DefaultRouter()
router.register(r"movies", MovieAPISet, basename="movies")
urlpatterns = [
    path("api/v1/", include(router.urls)),
]
