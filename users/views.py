from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from cars.serializers import UserRegistrationCheckInputSerializer, UserLoginOutputSerializer, UserLoginInputSerializer, \
    UserUpdateInputSerializer, UserRegistrationInputSerializer, UserRetrieveOutputSerializer
from users.selectors import UserSelector
from users.services import UserService

user_service = UserService()
user_selector = UserSelector()


class UserRegistrationAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginOutputSerializer

    @extend_schema(
        request=UserRegistrationInputSerializer,
        responses={HTTP_200_OK: serializer_class, HTTP_400_BAD_REQUEST: None}
    )
    def post(self, request):
        """Registers a new user and returns a token."""
        serializer = UserRegistrationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_service.create_user(**serializer.validated_data)
        return Response(self.serializer_class({"token": user.token.key}).data, status=HTTP_200_OK)


class UserRegistrationCheckAPI(APIView):
    permission_classes = (AllowAny,)
    serializer = UserRegistrationCheckInputSerializer

    @extend_schema(request=serializer, responses={HTTP_204_NO_CONTENT: None, HTTP_400_BAD_REQUEST: None})
    def post(self, request):
        """Checks if the phone number is already taken. Return 204 if it is not and 400 if it is."""
        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=HTTP_204_NO_CONTENT)


class UserLoginAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginOutputSerializer

    @extend_schema(
        request=UserLoginInputSerializer,
        responses={HTTP_200_OK: serializer_class, HTTP_400_BAD_REQUEST: None}
    )
    def post(self, request):
        """Returns a user token."""
        serializer = UserLoginInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = user_selector.get_user_token_by_credentials(**serializer.validated_data)
        return Response(self.serializer_class(token).data, status=HTTP_200_OK)


class UserSelfRetrieveUpdateAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserRetrieveOutputSerializer

    def get(self, request):
        """Returns information about the user."""
        user = request.user
        return Response(self.serializer_class(user).data, status=HTTP_200_OK)

    @extend_schema(
        request=UserUpdateInputSerializer,
        responses={HTTP_204_NO_CONTENT: None, HTTP_400_BAD_REQUEST: None}
    )
    def patch(self, request):
        """Modifies information about the user."""
        user = request.user
        serializer = UserUpdateInputSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user_service.update_user(user, **serializer.validated_data)
        return Response(status=HTTP_200_OK)