from django.shortcuts import render
from .models import Contacto


#la vista debe tener el mismo nombre de la carpeta contacto del template
# es decir carpeta contacto ;vista contacto.
def index(request):
    #filtra todos los valores que contengan el search, sino traelos todos
    contactos = Contacto.objects.filter(nombre__contains=request.GET.get('search', ''))#se filtran los contactos por el nombre que se ingrese en el buscador
    contexto = {'contactos':contactos}#se crea un diccionario con los contactos
    return render(request, "contacto/index.html", contexto)#se renderiza el template index.html con el diccionario de contactos

    




