from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from users.constants.roles import Role
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=7, choices=Role.values(), default=Role.USER)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email
