from django.contrib import admin
from .models import Marca, ModeloAuto, TipoCombustible,DirectorEjecutivo

# Register your models here.
admin.site.register(Marca)
admin.site.register(ModeloAuto)
admin.site.register(TipoCombustible)
admin.site.register(DirectorEjecutivo)
