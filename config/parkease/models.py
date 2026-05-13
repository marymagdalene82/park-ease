from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
# User Model
class User(AbstractUser):

    ROLE_CHOICES = [
        ("attendant", "Parking Attendant"),
        ("tyre_manager", "Tyre Manager"),
        ("battery_manager", "Battery Manager"),
        ("admin", "System Admin"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# VEHICLE MODEL
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
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="vehicles"
    )

    def __str__(self):
        return self.name

# PARKING SESSION MODEL
class ParkingSession(models.Model):
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="parking_sessions"
    )
    receipt_number = models.CharField(max_length=20, unique=True, editable=False)
    arrival_time = models.DateTimeField(default=timezone.now)
    departure_time = models.DateTimeField(blank=True, null=True)
    receiver_name = models.CharField(max_length=100, blank=True, null=True)
    receiver_phone = models.CharField(max_length=10, blank=True, null=True)
    receiver_nin = models.CharField(max_length=20, blank=True, null=True)
    parking_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_signed_out = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_sessions"
    )
    signed_out_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="signed_out_sessions",
    )
    created_at = models.DateTimeField(auto_now_add=True)


# TYRE SERVICE MODEL
class TyreService(models.Model):
    SERVICE_TYPE_CHOICES = [
        ("pressure", "Pressure"),
        ("puncture", "Puncture Fixing"),
        ("valve", "Valve"),
    ]
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="services"
    )
    service_date = models.DateField(auto_now_add=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="services_recorded"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} for {self.vehicle}"


# BATTERY SERVICE MODEL
class BatteryTransaction(models.Model):

    TRANSACTION_TYPES = [
        ("hire", "Hire"),
        ("sale", "Sale"),
    ]

    BATTERY_PRICES = {
        "hire": 10000,
        "sale": 250000,
    }
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.SET_NULL, null=True, blank=True
    )

    customer_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=10)

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    battery_type = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    transaction_date = models.DateTimeField(default=timezone.now)

    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

