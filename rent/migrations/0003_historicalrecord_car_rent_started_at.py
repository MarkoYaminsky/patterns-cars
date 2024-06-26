# Generated by Django 5.0.6 on 2024-05-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0002_alter_car_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ended", "Ended"), ("canceled", "Canceled")],
                        max_length=10,
                    ),
                ),
                ("car_id", models.IntegerField()),
                ("car_name", models.CharField(max_length=100)),
                ("started_at", models.DateTimeField()),
                ("finished_at", models.DateTimeField()),
                ("initial_deposit_in_dollars", models.IntegerField()),
                ("price_per_day_in_dollars", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="rent_started_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
