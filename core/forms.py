from django import forms
from .models import CustomUser, dispositivos

class usuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nombre_usuario', 'email_usuario', 'password']

class dispositivoForm(forms.ModelForm):
    class Meta:
        model = dispositivos
        fields = '__all__'
        widgets = { 'fecha_dispositivos': forms.DateInput(attrs={'type': 'date'})}
