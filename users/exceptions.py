from common.exceptions import BaseCustomException


class UserWithPhoneNumberAlreadyExistsError(BaseCustomException):
    def __init__(self, phone_number: str) -> None:
        detail = f"User with phone number {phone_number} already exists."
        super().__init__(detail=detail)


class NoAuthTokenError(BaseCustomException):
    def __init__(self, phone_number: str) -> None:
        detail = f"User with phone {phone_number} has no authentication token."
        super().__init__(detail=detail)


class InvadlidCredentialsError(BaseCustomException):
    def __init__(self) -> None:
        detail = "Phone number or password is invalid."
        super().__init__(detail=detail)
