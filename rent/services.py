from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from common.services import CommonService
from rent.models import Car
from rent.selectors import CarSelector

User = get_user_model()


class CarService:
    car_selector = CarSelector()
    common_service = CommonService()

    def rent_car(self, car: Car, user: User) -> None:
        self.common_service.update_instance(
            instance=car,
            data={
                "current_owner": user,
                "rent_to": datetime.now() + timedelta(days=car.renting_period_in_days),
            },
        )

    def return_car(self, car: Car) -> None:
        car.current_owner = None
        if car.rent_to <= datetime.now():
            car.fines.append("Late return")
        car.rent_to = None
        car.save()

    def add_fine(self, car: Car, fine: str) -> None:
        car.fines.append(fine)
        car.save()
