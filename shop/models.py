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


class Tableta(models.Model):
    serietableta = models.CharField(max_length=50, primary_key=True, db_column='SerieTableta')
    sistem_operare = models.CharField(max_length=50, db_column='SistemOperare')
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacitate_ram = models.CharField(max_length=50, db_column='CapacitateRAM')
    capacitate_memorie = models.CharField(max_length=50, db_column='CapacitateMemorie')
    culoare = models.CharField(max_length=50)
    lungime = models.IntegerField()
    latime = models.IntegerField()
    unitati_masura = models.CharField(max_length=20, db_column='UnitatiMasura')
    grosime = models.IntegerField()
    greutate = models.IntegerField()
    capacitate_acumulator = models.IntegerField(db_column='CapacitateAcumulator')
    rezolutie = models.IntegerField()
    diagonala = models.IntegerField()
    conectivitate = models.CharField(max_length=20)
    model_procesor = models.CharField(max_length=50, db_column='ModelProcesor')
    pret = models.IntegerField(null=True)
    nota_produs = models.FloatField(null=True, db_column='NotaProdus')
    disponibilitate = models.CharField(max_length=100, null=True)
    optiune_livrare = models.CharField(max_length=100, null=True, db_column='OptiuneLivrare')

    class Meta:
        db_table = 'tablete'

    def __str__(self):
        return f"{self.brand} {self.model} - {self.pret} RON"

