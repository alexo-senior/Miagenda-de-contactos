from django.shortcuts import render
from . import views
from .models import ToDo

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


def edit(request, edit):
    
    return render(request, "toDo/index.html",{})



def create(request):
    return render(request, "toDo/index.html", contexto)


def delete(request, id):
    return render(request, "toDo/index.html", contexto)



    






