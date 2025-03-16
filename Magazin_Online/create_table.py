# create_laptop.py
import os
import django

# Setează variabila de mediu pentru setările Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Magazin_Online.settings')

# Inițializează Django
django.setup()

# Acum poți importa modelele și să lucrezi cu baza de date
from Magazin_Online.models import Laptop

# Creează un Laptop în baza de date
laptop = Laptop(name="Laptop 1", price=1000, description="Laptop performant")
laptop.save()

# Verifică dacă a fost adăugat
laptops = Laptop.objects.all()
for laptop in laptops:
    print(f'{laptop.name}: {laptop.price} Lei')
