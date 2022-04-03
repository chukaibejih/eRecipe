from django.urls import path
from rest_framework.routers import SimpleRouter

from accounts import views

router = SimpleRouter()
register = views.UserViewSet.as_view({"post": "create"})

router.register ("", views.UserViewSet, basename="users")
router.register ("user-profiles", views.UserProfileViewSet, basename="user-profiles")

urlpatterns = router.urls
