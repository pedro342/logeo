from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import View
from .forms import usuarioForm, dispositivoForm
from .models import dispositivos, CustomUser
from django.contrib.auth import login, logout, authenticate



# Create your views here.

def home(request):
    return render(request, 'core/home.html')

#def dispositivosView(request):
#    return render(request, 'core/dispositivos.html')

def exit(request):
    logout(request)
    return redirect('home')

#def registrar(request):
#   return render(request, 'registration/registrar.html')

#def registrarDispo(request):
#    return render(request, 'registration/registrarDispositivo.html')

class formularioUsuariosView(View):

    def get(self, request):
        usuarioVar = usuarioForm()
        return render(request, 'registration/registrar.html', {'form': usuarioVar})
    
    def post(self, request):
        usuarioVar = usuarioForm(request.POST)
        if request.method == 'POST':
            nombre_usuario = request.POST['nombre_usuario']
            email_usuario = request.POST['email_usuario']
            password = request.POST['password']
            user = CustomUser.objects.create_user(nombre_usuario=nombre_usuario, email_usuario=email_usuario, password=password)
        return render(request, 'registration/registrar.html', {'form': usuarioVar, "mensaje": 'OK'})

class formularioDispositivoView(View):

    def get(self, request):
        dispositivosVar = dispositivoForm()
        return render(request, 'registration/registrarDispositivo.html', {"formDisp": dispositivosVar})

    def post(self, request):
        dispositivosVar = dispositivoForm(request.POST)
        if dispositivosVar.is_valid():
            dispositivosVar.save()
            dispositivosVar = dispositivoForm()
        return redirect('registrarDispositivos')

@login_required
def listar_dispositivos(request):
    dispositivosVar = dispositivos.objects.all()
    return render(request, 'core/dispositivos.html', {"dispositivosDic": dispositivosVar})

def loginView(request):
    if request.method == 'POST':
        username = request.POST['nombre_usuario']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')

def logoutView(request):
    logout(request)
    return redirect('home')