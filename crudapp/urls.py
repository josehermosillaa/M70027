from django.urls import path
from . import views
urlpatterns = [
    path("",views.insertar_emp,name ="insertar-emp"),
    path("mostrar/",views.mostrar_emp,name ="mostrar-emp"),
    path("eliminar/<int:id>/",views.eliminar_emp,name ="eliminar-emp"),
    path("editar/<int:id>/",views.editar_emp,name ="editar-emp"),
]