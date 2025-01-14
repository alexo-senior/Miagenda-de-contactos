from django.contrib import admin
from .models import ToDo


# Register your models here.
from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    # Especifica los campos que deseas mostrar en el formulario de edición
    fields = ('titulo', 'descripcion', 'prioridad', 'tiempo_estimado', 'fecha_creacion')
    # Especifica los campos que deseas mostrar en la lista del admin
    list_display = ('titulo', 'prioridad', 'tiempo_estimado', 'fecha_creacion','fecha_finalizacion')
    # Para que `fecha_creacion` no sea editable en el formulario, puedes usar `readonly_fields`
    readonly_fields = ('fecha_creacion',)

# Registra el modelo y la clase de administración
admin.site.register(ToDo, ToDoAdmin)







