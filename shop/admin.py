from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('serielaptop', 'brand', 'model', 'pret', 'disponibilitate')
    search_fields = ('brand', 'model', 'procesor')
