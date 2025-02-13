from django.urls import path
from .import views
#en django , cuando se crean parametros opcionales como letter, se debe colocar adicional a la ruta principal 
#del index,este no se puede alterar, es decir, si se coloca una ruta con el nombre index, no se puede colocar otra
#con el mismo nombre, pero si se puede colocar una con el nombre index y un parametro adicional

urlpatterns = [
    path('', views.index, name='contactos'),
    path('contactos/<str:letter>/', views.index, name='contactos'),
    path('view/<int:id>', views.view, name='view'),#se crea una ruta con el nombre view que recibe un parametro id
    path('edit/<int:id>', views.edit, name='edit'),#se crea una ruta con el nombre edit que recibe un parametro id
    path('create/', views.create, name='create'),#se crea una ruta con el nombre create
    path('delete/<int:id>',views.delete, name='delete'),#se crea una ruta con el nombre delete
    
        
    ] 



