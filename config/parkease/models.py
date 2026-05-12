from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User Model
class User(AbstractUser):

    ROLE_CHOICES = [
        ('attendant', 'Parking Attendant'),
        ('tyre_manager', 'Tyre Manager'),
        ('battery_manager', 'Battery Manager'),
        ('admin', 'System Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Vehicle_registration(models.Model):
    driver_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    Vehicle_type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    nin = models.CharField(max_length=20, blank=True, null=True)  
    arrival_time = models.TimeField()
    arrival_date = models.DateField()
    receipt_number = models.CharField(max_length=50, unique=True)  
    is_signed_out = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehicles")
    
    def __str__(self):
        return self.name

# VEHICLE MODEL

# PARKING SLOT MODEL


# TYRE SERVICE MODEL

class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Pressure', 'Puncture Repair'),
        ('Valve', 'Valve Replacement'),
    ]
 # Ai developed the top part I'm not quite sure

    service_date = models.DateField(auto_now_add=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    vehicle = models.ForeignKey(Vehicle_registration, on_delete=models.CASCADE, related_name="services")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="services_recorded")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} for {self.vehicle}"
 #This too

# BATTERY SERVICE MODEL

