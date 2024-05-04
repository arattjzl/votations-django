from django.urls import path
from . import views

urlpatterns = [
    path('votacion/', views.votacion, name='votacion'),
    path('conteo_votos/', views.conteo_votos, name='conteo_votos'),
    path('voto/<int:id>', views.voto, name='voto'),
    path('grafica/', views.grafica, name='grafica'),
]