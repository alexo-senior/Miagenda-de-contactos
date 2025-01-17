from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contactos/', views.contactos, name='contactos'),
    path('toDo/', views.toDo, name='toDo'),
]

