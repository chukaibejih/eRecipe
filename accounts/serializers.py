from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import UserProfile

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    # Overide default token login to include `user` data
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            "id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "username": self.user.username,
            "email": self.user.email,
            "is_superuser": self.user.is_superuser,
            "is_staff": self.user.is_staff,
            "is_verified": self.user.is_verified
        })

        return data



class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = [
            "last_login",
            "date_joined",
            "is_organization",
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
        return User.objects.create_user(email, password, **validated_data)


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
            "is_active",
            "is_verified",
            "user_profile",
        ]
        
    def get_user_profile(self, obj):
        try:
            return UserProfileSerializer(obj.profile).data

        except:
            return None


class ChangePasswordSerializer(serializers.Serializer):
    
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
