from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
