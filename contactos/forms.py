
from django.forms import ModelForm
from .models import contacto

class ContactoForm(ModelForm):
    class Meta:
        model = contacto
        #fields = '__all__'# de esta forma se llama a todos los campos d ela tabla contacto
        fields = ['nombre', 'telefono',
                'date', 'apellidos', 'movil',
                'email', 'direccion', 'compañia',
                'fecha_nacimiento', 'notas']
        
        
        # Agregando ayuda a los campos
        help_texts = {
            'nombre': 'Ingrese su nombre completo',
            'telefono': 'Ingrese su número de teléfono fijo',
            'movil': 'Ingrese su número de teléfono móvil',
            'email': 'Ingrese su dirección de correo electrónico',
            'fecha_nacimiento': 'Ingrese su fecha de nacimiento en formato DD/MM/AAAA',
        }
        
        
        # Personalizando los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio',
            },
            'telefono': {
                'required': 'El teléfono es obligatorio',
            },
            'email': {
                'required': 'El correo electrónico es obligatorio',
                'invalid': 'Ingrese una dirección de correo electrónico válida',
            },
        }
        
        