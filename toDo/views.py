from django.shortcuts import render, redirect ,get_object_or_404
from . import views
from django.contrib import messages
from .models import ToDo
from .forms import  ToDoForm




#Vista de index 

def index(request):
    search_query = request.GET.get('search', '')#
    Todo = ToDo.objects.filter(titulo__icontains=search_query)
    contexto ={
        'Todo':Todo
    }
    return render(request, "toDo/index.html", contexto)#se renderiza la plantilla index.html con el contexto


def view(request, id):
    todo = ToDo.objects.get(id=id)#se obtiene la tarea con el id que se pasa como parametro
    contexto = {'todo': todo}#se crea un diccionario con la tarea
    return render(request, "toDo/detail.html", contexto)#se renderiza la plantilla detail.html con el contexto


# FUNCION PARA EDICION DE TAREAS

def edit(request, id):
    todo = get_object_or_404(ToDo, id=id)  # Manejo de errores
    
    if request.method == 'GET':
        form = ToDoForm(instance=todo)  # Cargar el formulario con la instancia
        contexto = {
            'form': form, 
            'id': id}
        
        return render(request, "toDo/edicion.html", contexto)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)  # Crear formulario con datos POST
        if form.is_valid():
            form.save()
        messages.success(request, 'Tarea editada con éxito')  # Mensaje de éxito
            #return redirect('toDo')  # Redirigir a la lista de tareas

        contexto = {
        'form': form,
        'id': id
        }
    
        return render(request, "toDo/edicion.html", contexto)

#FUNCION PARA CREAR TAREAS        
    
def create(request):
    if request.method == 'GET':
        form = ToDoForm()
        contexto = {
            'form':
                form
        }
        return render(request, 'toDo/create.html', contexto)
    
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('toDo')
        
    
    
#FUNCION PARA ELIMINAR TAREAS

def delete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect('toDo')



    



    






