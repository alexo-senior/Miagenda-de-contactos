from django.shortcuts import render
from .models import Contacto
from .forms import ContactoForm

def index(request):
    contactos = Contacto.objects.filter(nombre__contains=request.GET.get('search', ''))#se filtran los contactos por el nombre
    contexto = {'contactos': contactos}#se crea un diccionario con los contactos
    return render(request, "contacto/index.html", contexto)#se renderiza la plantilla index.html con el contexto

def view(request, id):
    contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
    contexto = {'contacto': contacto}#se crea un diccionario con el contacto
    return render(request, "contacto/detail.html", contexto)#se renderiza la plantilla detail.html con el contexto

def edit(request, id):
    if request.method == 'GET':#si el metodo es GET
        contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
        form = ContactoForm(instance=contacto)#se crea un formulario con los datos del contacto
        contexto = {'form': form}#se crea un diccionario con el formulario
        return render(request, 'contacto/create.html', contexto)#se renderiza la plantilla create.html con el contexto
    
    
