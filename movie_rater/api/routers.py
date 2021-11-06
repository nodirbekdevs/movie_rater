from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('rating', RatingViewSet)
router.register('users', UserViewSet)