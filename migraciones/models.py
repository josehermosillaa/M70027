from django.db import models

# Create your models here.
class PrecioHistoricoVehiculos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del Precio")
    modelo = models.TextField()
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    color = models.CharField(max_length=50, default="Desconocido", verbose_name="Color")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "precio historico"
        verbose_name_plural = "precios historicos"
        ordering = ["-created"]
    
    def __str__(self):
        return self.modelo
