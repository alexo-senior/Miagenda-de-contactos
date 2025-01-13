from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='contactos'),
    path('view/<int:id>', views.view, name='view'),#se crea una ruta con el nombre view que recibe un parametro id
    path('edit/<int:id>', views.edit, name='edit'),#se crea una ruta con el nombre edit que recibe un parametro id
    path('create/', views.create, name='create'),#se crea una ruta con el nombre create
    path('delete/<int:id>',views.delete, name='delete'),#se crea una ruta con el nombre delete
        
    ] 


