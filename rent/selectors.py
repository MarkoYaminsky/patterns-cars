from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from rent.models import Car

User = get_user_model()


class CarSelector:
    def get_all_cars(self) -> QuerySet[Car]:
        return Car.objects.all().order_by("current_owner")

    def get_available_cars(self) -> QuerySet[Car]:
        return Car.objects.filter(current_owner=None)

    def get_user_cars(self, user: User) -> QuerySet[Car]:
        return Car.objects.filter(current_owner=user)

    def get_car_by_id(self, car_id: int) -> Car:
        return Car.objects.get(id=car_id)

    def get_price_for_rent(self, car: Car) -> int:
        return (
            car.daily_price_in_dollars * car.renting_period_in_days
            + car.initial_deposit_in_dollars
        )
