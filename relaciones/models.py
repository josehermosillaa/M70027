import datetime
from django.db import models


# Create your models here.


def anno_actual():
    return datetime.date.today().year

ANNO_CHOICES = []
for r in range(1950, anno_actual()+1):
    ANNO_CHOICES.append((r,r))
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Marca Auto")
    pais = models.CharField(max_length=255, verbose_name="Pais")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
        ordering = ["-created"]
    

    def __str__(self):
        return self.nombre

class DirectorEjecutivo(models.Model):
    nombre = models.CharField(max_length=255,blank=True, verbose_name="Director Ejecutivo")
    marca = models.OneToOneField(Marca, verbose_name="Marca", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")
    class Meta:
        verbose_name = "director ejecutivo"
        verbose_name_plural = "directores ejecutivos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Combustible")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "combustible"
        verbose_name_plural = "combustibles"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre

class ModeloAuto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Modelo Auto")
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Marca auto")
    tipo_combustible = models.ManyToManyField(TipoCombustible, verbose_name="Combustible(s)")
    f_fabricacion = models.IntegerField(choices=ANNO_CHOICES, default=anno_actual(),verbose_name="Fecha Fabricacion")
    costo_fabricacion = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name="Costo fabricacion")
    precio_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10, verbose_name="Precio Venta")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre
