from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from . import serializers
from .models import User, UserProfile

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
     list: List all users on the platform
    create: Register/Sign up a new user on the platform
    partial_update: Update a user profile
    destroy: Delete a user from the platform

    """

    serializer_class = serializers.RetrieveUserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.RegisterUserSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        if self.action == "destroy":
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return super().get_permissions()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    list all users
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "patch"]

    def get_permissions(self):
        return super().get_permissions(self)
        if self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), custom_permissions.IsOwnerOrReadOnly]
        return super().get_permissions()
