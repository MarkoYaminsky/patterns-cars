from datetime import datetime, timedelta

from django.contrib.auth import get_user_model

from common.services import CommonService
from common.singletone import Singletone
from rent.models import Car, HistoricalRecord
from rent.selectors import CarSelector

User = get_user_model()


class HistoricalRecordService(Singletone):
    def create_record(
        self, car: Car, user: User, status: HistoricalRecord.Status
    ) -> HistoricalRecord:
        renting_period_in_days = (car.rent_to - car.rent_started_at).days + 1
        return HistoricalRecord.objects.create(
            user=user,
            car_id=car.id,
            status=status,
            car_name=str(car),
            started_at=car.rent_started_at,
            finished_at=datetime.now(),
            initial_deposit_in_dollars=car.initial_deposit_in_dollars,
            price_per_day_in_dollars=car.daily_price_in_dollars,
            is_finished_on_time=car.rent_to >= datetime.now(),
            renting_period_in_days=renting_period_in_days,
        )


class CarService(Singletone):
    def rent_car(self, car: Car, user: User) -> None:
        CommonService().update_instance(
            instance=car,
            data={
                "current_owner": user,
                "rent_to": datetime.now() + timedelta(days=car.renting_period_in_days),
                "rent_started_at": datetime.now(),
            },
        )

    def return_car(self, car: Car, is_canceled: bool, user: User) -> None:
        if car.rent_to <= datetime.now():
            self.add_fine(car, "Late return")
        HistoricalRecordService().create_record(
            car,
            status=(
                HistoricalRecord.Status.CANCELED
                if is_canceled
                else HistoricalRecord.Status.ENDED
            ),
            user=user,
        )
        CommonService().update_instance(
            instance=car,
            data={"rent_started_at": None, "rent_to": None, "current_owner": None},
        )

    def add_fine(self, car: Car, fine: str) -> None:
        car.fines.append(fine)
        car.save()
