from django.contrib import admin
from .models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('serielaptop', 'brand', 'model', 'pret', 'disponibilitate')
    search_fields = ('brand', 'model', 'procesor')

from .models import Tableta

@admin.register(Tableta)
class TabletaAdmin(admin.ModelAdmin):
    list_display = ('SerieTableta', 'Brand', 'Model', 'pret', 'Disponibilitate')
    search_fields = ('SerieTableta', 'Brand', 'Model')
    list_filter = ('Brand', 'Disponibilitate', 'SistemOperare')