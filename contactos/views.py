from django.shortcuts import render

#la vista debe tener el mismo nombre de la carpeta contacto del template
# es decir carpeta contacto ;vista contacto.
def index(request):
    return render(request, "contacto/index.html", {})

