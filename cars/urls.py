from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/download/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("users/", include("users.urls", namespace="users")),
]

