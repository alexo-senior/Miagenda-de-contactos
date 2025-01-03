from django.shortcuts import render

def index(request):
    # ...existing code...

def contactos(request):
    # Define la lógica para la vista 'contactos'
    return render(request, 'contactos.html')

def toDo(request):
    # ...existing code...