from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_partidos, name='lista_partidos'),
    path('nuevo/', views.nuevo_partido, name='nuevo_partido'),
    path('editar/<int:id>', views.editar_partido, name='editar_partido'),
    path('eliminar/<int:id>', views.eliminar_partido, name='eliminar_partido'),
]