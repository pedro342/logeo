from django.urls import path
from .views import home, dispositivos

urlpatterns = [
    path('home/', home, name='home'),
    path('dispositivos/', dispositivos, name='dispositivos'),
]
