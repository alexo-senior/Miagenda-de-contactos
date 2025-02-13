from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.contrib import messages
from django.http import HttpResponse



#filtrar los contactos por nombre
#aqui se colocar letter como parametro opcional para poder filtrar los contactos por la letra que empieza el nombre
#si no se coloca nada en la url, se muestran todos los contactos

def index(request, letter=None):
    print(f"Letra recibida: {letter}")
    if letter != None:#si letter es diferente de None
        #return HttpResponse('Mostrar contactos que empiecen con la letra ' + letter)#se retorna un mensaje
        contactos = Contacto.objects.filter(nombre__istartswith=letter)#se filtran los contactos por la letra que empieza el nombre
    else:
        query = request.GET.get('search', '')#se obtiene el valor del input search
        if query:
            contactos = Contacto.objects.filter(nombre__icontains=query) # Filtra por coincidencia en el nombre
        else:
            contactos = Contacto.objects.all()#se obtienen todos los contactos
        
    contexto = {'contactos': contactos}#se crea un diccionario con los contactos
    return render(request, "contacto/index.html", contexto)#se renderiza la plantilla index.html con el contexto
        

    


#obtener los contactos por el id

def view(request, id):
    contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
    contexto = {'contacto': contacto}#se crea un diccionario con el contacto
    return render(request, "contacto/detail.html", contexto)#se renderiza la plantilla detail.html con el contexto

#editar  contactos por el id


def edit(request, id):
    contacto = get_object_or_404(Contacto, id=id)#se obtiene el contacto con el id que se pasa como parametro
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
    
    
    
    # crear contactos, primero hacemos un get si el metodo es GET, si es POST se crea un contacto
def create(request):
    if request.method == 'GET':#si el metodo es GET
        form = ContactoForm#se crea un formulario
        contexto = {'form': form}#se crea un diccionario con el formulario
        return render(request, 'contacto/create.html', contexto) #se renderiza la plantilla create.html con el contexto
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)#se crea un formulario con los datos del contacto
        if form.is_valid():
            form.save()
        return redirect('contactos')#se redirige a la ruta contactos
        messages.success(request, 'Contacto creado correctamente')
        
        
#en la vida real no se debe hacer el borrado a traves de una url, me refiero a html
# se debe hacer a traves de un formulario, asi evitas que alguien borre un contacto sin querer
#o de forma maliciosa        
        
def delete(request, id):
    contacto = Contacto.objects.get(id=id)#se obtiene el contacto con el id que se pasa como parametro
    contacto.delete()#se elimina el contacto
    return redirect('contactos')#se redirige a la ruta contactos en general ojo que no se redirige a la ruta index
    messages.success(request, 'Contacto eliminado correctamente')#se muestra un mensaje de exito
    
    
    
    

    
    
    
    
    
    

    
    
