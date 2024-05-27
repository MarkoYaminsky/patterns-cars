from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from rent.models import Car
from rent.selectors import CarSelector
from rent.serializers import CarOutputSerializer
from rent.services import CarService

car_selector = CarSelector()
car_service = CarService()


class AvailableCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return car_selector.get_available_cars()


class AllCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return car_selector.get_all_cars()


class MyCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return car_selector.get_user_cars(self.request.user)


class CarDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get(self, request, car_id):
        """Returns car details by id."""
        car = get_object_or_404(Car, id=car_id)
        serializer = CarOutputSerializer(car)
        return Response(serializer.data, status=HTTP_200_OK)


class RentCarAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=None, responses={HTTP_204_NO_CONTENT: None, HTTP_404_NOT_FOUND: None}
    )
    def post(self, request, car_id):
        """Rent a car."""
        car = get_object_or_404(Car, id=car_id)
        car_service.rent_car(car, request.user)
        return Response(status=HTTP_204_NO_CONTENT)


class ReturnCarAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=None, responses={HTTP_204_NO_CONTENT: None, HTTP_404_NOT_FOUND: None}
    )
    def post(self, request, car_id):
        """Return a car."""
        car = get_object_or_404(Car, id=car_id)
        car_service.return_car(car)
        return Response(status=HTTP_204_NO_CONTENT)