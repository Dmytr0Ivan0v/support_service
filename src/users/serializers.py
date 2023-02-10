from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerialiser(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]


class UserGetSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
