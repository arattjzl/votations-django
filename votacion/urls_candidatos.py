from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_candidatos, name='lista_candidatos'),
    path('nuevo/', views.nuevo_candidato, name='nuevo_candidato'),
    path('editar/<int:id>', views.editar_candidato, name='editar_candidato'),
    path('eliminar/<int:id>', views.eliminar_candidato, name='eliminar_candidato'),
]