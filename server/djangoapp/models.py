from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100, default="USA")  # 可选字段
    founded_year = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.name} - {self.country}"


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')

    year = models.IntegerField(
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ],
        default=2023
    )

    dealer_id = models.IntegerField()  # Refers to Cloudant dealer

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
