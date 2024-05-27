from rest_framework import serializers

from common.serializers import BaseStringOutputSerializer
from .models import Car, HistoricalRecord
from .selectors import CarSelector


class CarOutputSerializer(BaseStringOutputSerializer):
    price_for_rent = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            "id",
            "make",
            "year",
            "daily_price_in_dollars",
            "current_owner",
            "number_of_seats",
            "type",
            "initial_deposit_in_dollars",
            "transmission_type",
            "fines",
            "description",
            "renting_period_in_days",
            "rent_to",
            "image_url",
            "price_for_rent",
        )

    def get_price_for_rent(self, car: Car) -> int:
        selector = CarSelector()
        return selector.get_price_for_rent(car)


class HistoricalRecordOutputSerializer(BaseStringOutputSerializer):
    total_price = serializers.IntegerField()
    started_at_ukrainian_format_datetime = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M:%S", source="started_at"
    )
    finished_at_ukrainian_format_datetime = serializers.DateTimeField(
        format="%d.%m.%Y %H:%M:%S", source="finished_at"
    )

    class Meta:
        model = HistoricalRecord
        fields = (
            "id",
            "status",
            "car_id",
            "car_name",
            "started_at",
            "finished_at",
            "is_finished_on_time",
            "renting_period_in_days",
            "initial_deposit_in_dollars",
            "price_per_day_in_dollars",
            "total_price",
            "started_at_ukrainian_format_datetime",
            "finished_at_ukrainian_format_datetime",
        )
