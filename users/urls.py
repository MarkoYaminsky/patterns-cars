from django.urls import path

from users.views import UserRegistrationAPI, UserRegistrationCheckAPI, UserLoginAPI, UserSelfRetrieveUpdateAPI

app_name = "users"

urlpatterns = [
    path("register/", UserRegistrationAPI.as_view(), name="user-registration"),
    path("register/check/", UserRegistrationCheckAPI.as_view(), name="user-registration-check"),
    path("login/", UserLoginAPI.as_view(), name="user-login"),
    path("me/", UserSelfRetrieveUpdateAPI.as_view(), name="me-retrieve-update"),
]
