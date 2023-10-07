from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', home, name='home'),
    path('dispositivos/', listar_dispositivos, name='dispositivosView'),
    path('registrarse/', formularioUsuariosView.as_view(), name='registrarUsuario'),
    path('registrarDispositivos/', formularioDispositivoView.as_view(), name='registrarDispositivos'),  
    path('loginAuthenticate/', loginView, name='loginAuth'),
    path('logout/', logoutView, name='logoutAuth'),
]