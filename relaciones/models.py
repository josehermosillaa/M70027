from django.db import models

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, verbose_name="Marca Auto")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")
    class Meta:
        verbose_name = "marca"
        verbose_name_plural = "marcas"
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
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.nombre
