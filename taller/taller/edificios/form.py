from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from edificios.models import *

class PropietarioForm(ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'cedula']

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio 
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']

class DeparatmentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario','nombrePropietario', 'costo', 'num_cuartos', 'edificio']
        
        