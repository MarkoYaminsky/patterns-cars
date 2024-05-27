from rest_framework import serializers

from .models import Car
from .selectors import CarSelector


class CarOutputSerializer(serializers.ModelSerializer):
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
