from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.contrib.postgres.fields import ArrayField

User = get_user_model()


class Car(models.Model):
    class Type(TextChoices):
        ELECTRO = "electro"
        PETROL = "petrol"

    class TransmissionType(TextChoices):
        AUTOMATIC = "automatic"
        MANUAL = "manual"

    make = models.CharField(max_length=100)
    year = models.IntegerField()
    daily_price_in_dollars = models.IntegerField()
    current_owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    number_of_seats = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=Type.choices)
    initial_deposit_in_dollars = models.IntegerField()
    transmission_type = models.CharField(
        max_length=10, choices=TransmissionType.choices
    )
    fines = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    description = models.TextField(blank=True)
    renting_period_in_days = models.IntegerField()
    rent_to = models.DateTimeField(blank=True, null=True)
    image_url = models.TextField(blank=True)

    def __str__(self):
        return f"{self.year} {self.make}"
