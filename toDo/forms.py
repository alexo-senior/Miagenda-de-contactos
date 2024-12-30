from django.forms import ModelForm  #importamos la clase ModelForm de django.forms
from .models import ToDo #importamos la clase ToDo del archivo models.py    



class ToDoForm(ModelForm): #creamos la clase ToDoForm que hereda de ModelForm
    class Meta: #creamos la clase Meta
        model = ToDo #indicamos que el modelo es toDo
        fields = '__all__' #indicamos que se van a mostrar todos los campos de la tabla ToDo
        
        
        
        

        
        
        