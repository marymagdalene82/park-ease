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
    
# VEHICLE MODEL

# PARKING SLOT MODEL


# TYRE SERVICE MODEL

# BATTERY SERVICE MODEL
