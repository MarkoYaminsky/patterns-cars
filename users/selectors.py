from typing import Any

from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet

from users.exceptions import InvadlidCredentialsError, NoAuthTokenError

User = get_user_model()


class UserSelector:
    def get_all_users(self, *args: Q, **kwargs: Any) -> QuerySet[User]:
        return User.objects.filter(*args, **kwargs)

    def get_user_by_phone_number(self, phone_number: str) -> User:
        return self.get_all_users(phone_number=phone_number).first()

    def get_user_token_by_credentials(self, phone_number: str, password: str) -> dict:
        user = self.get_all_users(phone_number=phone_number).first()

        if user is None or not user.check_password(password):
            raise InvadlidCredentialsError

        user_token = user.token
        if user_token is None:
            raise NoAuthTokenError(phone_number)

        return {"token": user_token.key}
