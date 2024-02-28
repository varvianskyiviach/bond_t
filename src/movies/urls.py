from rest_framework.routers import DefaultRouter

from movies.api import MovieAPISet

router = DefaultRouter()
router.register(r"movies", MovieAPISet, basename="movies")
urlpatterns = router.urls
