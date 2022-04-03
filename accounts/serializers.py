from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

User = get_user_model()



class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            "last_login",
            "date_joined",
            "user_permissions",
            "groups"
        ]
        extra_kwargs = {
            "is_active": {"read_only": True},
            "is_verified": {"read_only": True},
            "password": {"write_only": True},
            "user_permissions": {"read_only": True},
        }

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        username = validated_data.pop("username")
        return User.objects.create_user(email, password, username, **validated_data)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"
    

class RetrieveUserSerializer(serializers.ModelSerializer):

    user_profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "is_active",
            "is_verified",
            "user_profile",
        ]
        
    def get_user_profile(self, obj):
        try:
            return UserProfileSerializer(obj.profile).data

        except:
            return None
