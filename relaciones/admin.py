from django.contrib import admin
from .models import Marca, ModeloAuto, TipoCombustible,DirectorEjecutivo

# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'pais']
    list_display = ('id', 'nombre', 'pais')
    list_display_links = [ 'nombre']
    ordering = ('nombre', 'pais')

class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'f_fabricacion', 'costo_fabricacion','precio_venta', 'costo')
    ordering = ('marca',)
    list_display_links = ['nombre', 'marca']
    list_per_page = 4

    def costo(self, obj):
        return "Costo Alto" if obj.precio_venta >= 5000 else "Costo Bajo" 


admin.site.register(Marca, MarcaAdmin)
admin.site.register(ModeloAuto, ModeloAutoAdmin)
admin.site.register(TipoCombustible)
admin.site.register(DirectorEjecutivo)
