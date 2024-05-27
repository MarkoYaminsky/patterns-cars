from typing import Any, Optional

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from common.services import CommonService
from common.singletone import Singletone

User = get_user_model()


class UserService(Singletone):
    def create_user(
        self,
        phone_number: str,
        password: str,
        first_name: str,
        last_name: str,
        **kwargs: Any
    ) -> User:
        user = User.objects.create(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            **kwargs
        )
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user

    def update_user(self, user: User, **kwargs: Any) -> None:
        CommonService().update_instance(instance=user, data=kwargs)
