from django.shortcuts import render
from .models import Contacto
from .forms import ContactoForm
from django.contrib import messages


#filtrar los contactos por nombre

def index(request):
    contactos = Contacto.objects.filter(nombre__contains=request.GET.get('search', ''))#se filtran los contactos por el nombre
    contexto = {'contactos': contactos}#se crea un diccionario con los contactos
    return render(request, "contacto/index.html", contexto)#se renderiza la plantilla index.html con el contexto


#obtener los contactos por el id

def view(request, id):
    contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
    contexto = {'contacto': contacto}#se crea un diccionario con el contacto
    return render(request, "contacto/detail.html", contexto)#se renderiza la plantilla detail.html con el contexto

#editar o crear contactos por el id


def edit(request, id):
    contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
    if request.method == 'GET':#si el metodo es GET
        form = ContactoForm(instance=contacto)#se crea un formulario con los datos del contacto
        contexto = {'form': form, 'id': id}#se crea un diccionario con el formulario
        return render(request, 'contacto/edicion.html', contexto)#se renderiza la plantilla create.html con el contexto
    
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)#se crea un formulario con los datos del contacto
    if form.is_valid():
        form.save()
    messages.success(request, 'Contacto actualizado correctamente')#se muestra un mensaje de exito
    return render(request, 'contacto/edicion.html', {'form': form, 'id': id})#se renderiza la plantilla create.html con el formulario y el id
    #es un mensaje de django que se muestra en la plantilla create.html
    
        #return HttpResponse('Correcto')#si el metodo es POST se retorna un mensaje
    
    
    
        
    
    
    
