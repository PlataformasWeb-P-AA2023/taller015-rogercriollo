from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.IntegerField()

class Edificio(models.Model):
    opciones_tipo_Edificio = (
     
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
                            choices=opciones_tipo_Edificio)

    def _str_(self):
        return "%s %s %s %s" % (self.nombre,
                                self.direccion,
                                self.ciudad,
                                self.tipo)
    
    def obtener_cuartos(self):
        valor = [t.num_cuartos for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor
    
    def obtener_costosD(self):
        valor = [t.costo for t in self.Departamentos.all()]
        valor = sum(valor)
        return valor


  
    
    
class Departamento(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='propietarios')
    costo = models.FloatField()
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="Departamentos")

    def _str_(self):
        return "%s %s %d %s" % (self.nombrePropietario,
                self.costo,
                self.num_cuartos,
                self.edificio)
    
