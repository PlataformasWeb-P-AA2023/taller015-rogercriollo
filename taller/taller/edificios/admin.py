from django.contrib import admin

# Register your models here.

from edificios.models import *

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula')
    search_fields = ('nombre', 'apellido', 'cedula')

admin.site.register(Propietario, PropietarioAdmin)

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion')

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'costo', 'num_cuartos', 'edificio')

    raw_id_fields = ('propietario','edificio')

admin.site.register(Departamento, DepartamentoAdmin)