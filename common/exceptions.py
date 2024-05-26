from abc import ABC

from rest_framework.exceptions import ValidationError


class BaseCustomException(ABC, ValidationError):
    def __init__(self, detail: str):
        super().__init__({"detail": detail})
