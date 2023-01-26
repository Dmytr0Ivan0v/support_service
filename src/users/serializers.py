from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()


class UserCreateSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    @property
    def _writable_fields(self):
        for field in self.fields.values():
            if field.field_name == "password":
                field.write_only = True
            if not field.read_only:
                yield field

    def validate(self, attrs):
        attrs["password"] = make_password(attrs["password"])
        return attrs


class UserGetSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
