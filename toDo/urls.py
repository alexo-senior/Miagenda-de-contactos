from django.urls import path
from .import views



urlpatterns = [
    path('', views.index, name='toDo'),
    path('view/<int:id>', views.view, name='todo_view'),#se crea una ruta con el nombre view que recibe un parametro id
    path('edit/<int:id>', views.edit, name='todo_edit'),#se crea una ruta con el nombre edit que recibe un parametro id
    path('create/', views.create, name='todo_create'),#se crea una ruta con el nombre create
    path('delete/<int:id>',views.delete, name='todo_delete')
    ]


