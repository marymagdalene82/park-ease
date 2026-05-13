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

