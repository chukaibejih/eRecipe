from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets, permissions, status
from accounts import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import UserProfile

User = get_user_model()

from common import permissions as custom_permissions

class CustomTokenObtainPairViewset(TokenObtainPairView):
    
    # create: Login with email and password
    serializer_class = serializers.CustomTokenObtainPairSerializer


class UserViewset(viewsets.ModelViewSet):
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


class ChangePasswordViewset(generics.CreateAPIView):

    # Change password

    serializer_class = serializers.ChangePasswordSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["post"]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if not request.user.check_password(request.data.get("old_password")):
                return Response({"data": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            request.user.set_password(request.data.get("new_password"))
            request.user.save()
            return Response({"data": "Password changed successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserProfileViewset(viewsets.ModelViewSet):
    
    # list all users

    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "patch"]

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), custom_permissions.IsOwnerOrReadOnly()]
        return super().get_permissions()