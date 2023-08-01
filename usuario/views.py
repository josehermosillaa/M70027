from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistroUsuarioForm
# Create your views here.

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/crudapp/mostrar/')
        messages.error(request, "Registro Invalido. Algunos datos son incorrectos.")
    form = RegistroUsuarioForm()
    return render(request, "usuario/registro.html", context = {"register_form":form})
    

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"iniciaste sesion como {username}.")
                return HttpResponseRedirect( "/crudapp/mostrar/")
            else:
                messages.error(request, "username o password incorrectos")
                return HttpResponseRedirect("/usuario/login/")
        else:
            messages.error(request, "username o password incorrectos")
            return HttpResponseRedirect("/usuario/login/")      
    form = AuthenticationForm()
    return render(request, "usuario/login.html", context = {"login_form":form})
    

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesion satisfactoriamente")
    return HttpResponseRedirect("/usuario/login/")