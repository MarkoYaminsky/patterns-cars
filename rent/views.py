from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from rent.models import Car
from rent.selectors import CarSelector, HistoricalRecordSelector
from rent.serializers import CarOutputSerializer, HistoricalRecordOutputSerializer
from rent.services import CarService


class AvailableCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return CarSelector().get_available_cars()


class AllCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return CarSelector().get_all_cars()


class MyCarsListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarOutputSerializer

    def get_queryset(self):
        return CarSelector().get_user_cars(self.request.user)


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
        CarService().rent_car(car, request.user)
        return Response(status=HTTP_204_NO_CONTENT)


class ReturnCarAPI(APIView):
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        request=None,
        responses={HTTP_204_NO_CONTENT: None, HTTP_404_NOT_FOUND: None},
    )
    def post(self, request, car_id):
        """
        Returns a car.
        If the car rent is canceled, pass is_canceled=true in the query params.
        """
        car = get_object_or_404(Car, id=car_id)
        CarService().return_car(
            car,
            user=request.user,
            is_canceled=request.query_params.get("is_canceled") == "true",
        )
        return Response(status=HTTP_204_NO_CONTENT)


class HistoricalRecordListAPI(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HistoricalRecordOutputSerializer

    def get_queryset(self):
        return HistoricalRecordSelector().get_historical_records(self.request.user)
