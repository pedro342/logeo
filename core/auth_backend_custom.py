# custom_auth_backend.py
from django.contrib.auth.backends import ModelBackend
from .models import usuarios

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = usuarios.objects.get(username=usuarios.nombre_usuario)
            if user.check_password(password):
                return user
        except usuarios.DoesNotExist:
            return None
