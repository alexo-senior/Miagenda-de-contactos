from django.db import models
from datetime import date 

# Create your models here.
#se crea la clase contacto con los campos nombre, apellidos, telefono, email, direccion, fecha_nacimiento y foto
#la foto puede ser opcional dependiendo de las necesidades del usuario

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15,blank=False, null=False)
    movil = models.CharField(max_length=15, blank=True,null=True)
    email = models.EmailField(blank=True)
    direccion = models.TextField(blank=True, null=True)
    compañia = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    date = models.DateField(default=date.today)
    notas = models.TextField(blank=True, null=True)
        
    def __str__(self):
        return f"{self.nombre}"
    
    
    
    
    
    
    
    
    
    
    