from django.db import models

class Laptop(models.Model):
    serielaptop = models.CharField(max_length=50, primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tiplaptop = models.CharField(max_length=50)
    procesor = models.CharField(max_length=50)
    memorie_ram = models.IntegerField(db_column='MemorieRAM')  # <<<<< AICI E SECRETUL
    stocare = models.IntegerField()
    unitatimasura = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    porturi = models.CharField(max_length=50)
    sistemoperare = models.CharField(max_length=50)
    greutate = models.FloatField()
    pret = models.FloatField()
    notaprodus = models.IntegerField()
    disponibilitate = models.IntegerField()
    optiune_livrare = models.CharField(max_length=100, db_column='OptiuneLivrare')


    class Meta:
        db_table = 'laptopuri'


    def __str__(self):
        return f"{self.brand} {self.model} - {self.pret} RON"
