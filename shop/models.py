from django.db import models

class Laptop(models.Model):
    serielaptop = models.CharField(max_length=50, primary_key=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    tiplaptop = models.CharField(max_length=50)
    procesor = models.CharField(max_length=50)
    memorie_ram = models.IntegerField(db_column='MemorieRAM')
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
    SerieTableta = models.CharField(primary_key=True, max_length=50)
    SistemOperare = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    CapacitateRAM = models.CharField(max_length=50)
    CapacitateMemorie = models.CharField(max_length=50)
    Culoare = models.CharField(max_length=50)
    Lungime = models.IntegerField()
    Latime = models.IntegerField()
    UnitatiMasura = models.CharField(max_length=20)
    Grosime = models.IntegerField()
    Greutate = models.IntegerField()
    CapacitateAcumulator = models.IntegerField()
    Rezolutie = models.IntegerField()
    Diagonala = models.IntegerField()
    Conectivitate = models.CharField(max_length=20)
    ModelProcesor = models.CharField(max_length=50)
    pret = models.IntegerField(null=True, blank=True)
    NotaProdus = models.FloatField(null=True, blank=True)
    Disponibilitate = models.CharField(max_length=100, null=True, blank=True)
    OptiuneLivrare = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        db_table = 'tablete'

    def __str__(self):
        return f"{self.Brand} {self.Model}"

class Telefon(models.Model):
    SerieTelefon = models.CharField(max_length=50, primary_key=True, verbose_name='Cheie primară')
    SistemOperare = models.CharField(max_length=50)
    Brand = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    CapacitateRAM = models.IntegerField()
    CapacitateMemorie = models.IntegerField()
    Culoare = models.CharField(max_length=50)
    Lungime = models.IntegerField()
    Latime = models.IntegerField()
    Grosime = models.IntegerField()
    Diagonala = models.FloatField()
    Greutate = models.FloatField()
    CapacitateAcumulator = models.IntegerField()
    Material = models.CharField(max_length=50)
    Rezolutie = models.CharField(max_length=50)
    pret = models.IntegerField(null=True, blank=True)
    NotaProdus = models.FloatField(null=True, blank=True)
    Disponibilitate = models.CharField(max_length=100, null=True, blank=True)
    OptiuneLivrare = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'telefoane'
    def __str__(self):
        return f"{self.Brand} {self.Model} ({self.SerieTelefon})"