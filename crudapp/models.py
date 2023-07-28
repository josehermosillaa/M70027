from django.db import models

# Create your models here.

CHOICES_FIELDS = [
    ("Project Manager", "Project Manager"),
    ("Programador","Programador"),
    ("Soporte Técnico","Soporte Técnico"),
    ("Desarrollador Web", "Desarrollador Web")
]
class Empleado(models.Model):
    emp_id = models.CharField(max_length=3, verbose_name=" ID")
    emp_nombre = models.CharField(max_length=255, verbose_name="Nombre" )
    emp_correo = models.EmailField(verbose_name="Email")
    emp_designacion = models.CharField(max_length=150,choices=CHOICES_FIELDS, verbose_name="Designacion")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        db_table = "Employee"
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        ordering = ("emp_nombre", "-created")
        
    def __str__(self):
        return f"{self.emp_id} {self.emp_nombre} {self.emp_designacion}"
    