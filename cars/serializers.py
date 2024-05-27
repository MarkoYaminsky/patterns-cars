from users.exceptions import UserWithPhoneNumberAlreadyExistsError
from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.selectors import UserSelector

User = get_user_model()


class UserRegistrationCheckInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number",)


class UserRegistrationInputSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=20)
    middle_name = serializers.CharField(required=False, max_length=30)
    address = serializers.CharField(required=False, max_length=255)
    password = serializers.CharField()

    def validate_phone_number(self, phone_number: str) -> str:
        user_selector = UserSelector()
        if user_selector.get_user_by_phone_number(phone_number) is not None:
            raise UserWithPhoneNumberAlreadyExistsError(phone_number)
        return phone_number


class UserLoginInputSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()


class UserLoginOutputSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserRetrieveOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "phone_number",
            "first_name",
            "last_name",
            "middle_name",
            "address",
        )


class UserUpdateInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone_number", "first_name", "last_name", "middle_name", "address")
