from django.shortcuts import render
from .forms import VehicleForm

# Create your views here.
def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
    else:
        form = VehicleForm()

    context = {
        "form": form
    }
    return render(request, 'vehicle/vehicle_reg_form.html', context)



