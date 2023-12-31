from django.shortcuts import render, redirect
from .forms import EmpleadoForm
from .models import Empleado

# Create your views here.

#Insertar empleados
def insertar_emp(request):
    if request.method =="POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/crudapp/mostrar/")
    form = EmpleadoForm()
    context = {"form":form}
    return render(request, 'crudapp/insertar.html', context)

#obtener empleados
def mostrar_emp(request):
    empleados = Empleado.objects.all()
    num_visits = request.session.get('num_visits',1)
    request.session["num_visits"]= num_visits + 1
    context = {
        "empleados":empleados,
        "num_visits":num_visits,
        }
    return render(request, "crudapp/mostrar.html",context )

#editar empleados
def editar_emp(request, pk):
    if request.method == "POST":
        form =EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = Empleado.objects.get(pk=pk)
            empleado.emp_id = request.POST['emp_id']
            empleado.emp_nombre = request.POST['emp_nombre']
            empleado.emp_correo = request.POST['emp_correo']
            empleado.emp_designacion = request.POST['emp_designacion']
            empleado.save()
            return redirect('/crudapp/mostrar/')
    empleado = Empleado.objects.get(pk=pk)
    form = EmpleadoForm(instance=empleado)
    context = {'form':form, "empleado":empleado}
    return render(request, 'crudapp/editar.html', context)
    

#eliminar empleados
def eliminar_emp(request, pk):
    empleado = Empleado.objects.get(pk=pk)
    if request.method =="POST":
        empleado.delete()
        return redirect('/crudapp/mostrar/')
    context = {"empleado": empleado}
    return render(request, 'crudapp/eliminar.html', context)
        
def empleado_detalle(request, pk):
    empleado = Empleado.objects.get(id=pk)
    context = {
        'empleado':empleado,
    }
    return render(request, 'crudapp/detalle.html', context)

def inicio_view(request):
    return render(request, "crudapp/inicio.html")

def acerca_de_view(request):
    return render(request, "crudapp/acerca-de.html")
    