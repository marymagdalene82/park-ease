from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["driver_name", "phone_number", "vehicle_type", "model", "number_plate", "color", "nin"]
