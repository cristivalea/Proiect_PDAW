from django.shortcuts import render
from .models import Laptop

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'D:\\PDAW\\Magazin_Online\\templates\\laptop_list.html', {'laptops': laptops})
