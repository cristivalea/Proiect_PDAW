from django.db import models

class Laptop(models.Model):
    serielaptop = models.CharField(max_length=50, primary_key=True, verbose_name="Serielaptop")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tiplaptop = models.CharField(max_length=50, verbose_name="TipLaptop")
    procesor = models.CharField(max_length=50)
    memorie_ram = models.IntegerField(verbose_name="MemorieRAM")
    stocare = models.IntegerField(verbose_name="Stocare")
    unitati_masura = models.CharField(max_length=50, verbose_name="UnitateMasura")
    gpu = models.CharField(max_length=50, verbose_name="GPU")
    display = models.CharField(max_length=50, verbose_name="Display")
    porturi = models.CharField(max_length=50, verbose_name="Porturi")
    sistem_operare = models.CharField(max_length=50, verbose_name="SistemOperare")
    greutate = models.FloatField(verbose_name="Greutate")
    pret = models.FloatField(verbose_name="Pret")
    nota_produs = models.IntegerField(verbose_name="NotaProdus")
    disponibilitate = models.BooleanField(verbose_name="Disponibilitate")
    optiune_livrare = models.CharField(max_length=100, verbose_name="OptiuneLivrare")

    class Meta:
        db_table = 'laptopuri'

    def __str__(self):
        return f"{self.brand} {self.model} - {self.pret} RON"
