from django.urls import path

from rent.views import (
    AvailableCarsListAPI,
    MyCarsListAPI,
    AllCarsListAPI,
    CarDetailAPI,
    RentCarAPI,
    ReturnCarAPI,
)

app_name = "cars"

urlpatterns = [
    path("available/", AvailableCarsListAPI.as_view(), name="car-list"),
    path("my/", MyCarsListAPI.as_view(), name="my-cars"),
    path("all/", AllCarsListAPI.as_view(), name="all-cars"),
    path("<int:car_id>/", CarDetailAPI.as_view(), name="car-detail"),
    path("rent/<int:car_id>/", RentCarAPI.as_view(), name="rent-car"),
    path("return/<int:car_id>/", ReturnCarAPI.as_view(), name="return-car"),
]
