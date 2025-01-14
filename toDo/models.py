from django.db import models
from datetime import datetime

# Create your models here.
class ToDo(models.Model):
    #describe la prioridad de la tarea
    Eleccion_prioridad = [
        ('B','baja'),
        ('M', 'media'),
        ('A', 'alta')
    ]
    titulo = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tiempo_estimado = models.IntegerField(default=3)
    prioridad = models.CharField(max_length=1, choices=Eleccion_prioridad, default='B')  # Definición del campo prioridad
    fecha_finalizacion = models.DateTimeField(blank=True, null=True)
    
    #def __str__(self):
    #    return f"{self.titulo} {self.descripcion} {self.fecha_creacion}
        
    def __str__(self):
    # Truncar la descripción a 50 caracteres si es muy larga
        descripcion_truncada = self.descripcion[:50] + '...' if len(self.descripcion) > 50 else self.descripcion
        # get_prioridad_display(): Este método se utiliza
        # para obtener la representación legible de la elección de prioridad (baja, media, alta).
        return f"[{self.get_prioridad_display()}] {self.titulo} - {descripcion_truncada}"


    
    
    
    
    