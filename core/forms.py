from django import forms
from .models import dispositivos, usuarios

class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = '__all__'

class dispositivoForm(forms.ModelForm):
    class Meta:
        model = dispositivos
        fields = '__all__'
        widgets = { 'fecha_dispositivos': forms.DateInput(attrs={'type': 'date'})}
