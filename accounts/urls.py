from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from accounts import views

router = SimpleRouter()
register = views.UserViewset.as_view({"post": "create"})

router.register("", views.UserViewset, basename="users")
router.register("profile", views.UserProfileViewset)
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", views.CustomTokenObtainPairViewset.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("change-password/", views.ChangePasswordViewset.as_view(), name="change_password"),
    path("reset-password/", include("django_rest_passwordreset.urls", namespace="password_reset")),
]

urlpatterns += router.urls
