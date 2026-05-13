from django.db import models

# Create your models here.
class Vehicle(models.Model):

    VEHICLE_TYPES = [
        ("truck", "Truck"),
        ("car", "Personal Car"),
        ("taxi", "Taxi"),
        ("coaster", "Coaster"),
        ("boda", "Boda-boda"),
    ]

    driver_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    model = models.CharField(max_length=100)
    number_plate = models.CharField(
        max_length=10,
        unique=True,
    )
    color = models.CharField(max_length=50)
    nin = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return self.name

