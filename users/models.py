from typing import Optional

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_superuser(
            self, first_name: str, last_name: str, phone_number: str, password: str
    ) -> "User":
        from users.services import UserService

        return UserService().create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
            is_staff=True,
            is_superuser=True,
        )


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
        "password",
    )
    objects = UserManager()

    @property
    def token(self) -> Optional[Token]:
        return getattr(self, "auth_token", None)

    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"

    def __str__(self) -> str:
        return self.full_name
