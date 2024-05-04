from django.contrib import admin
from django.urls import path, include
from votacion.views import bienvenida
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('partidos/', include('votacion.urls_partidos')),
    path('candidatos/', include('votacion.urls_candidatos')),
    path('votaciones/', include('votacion.urls_votacion')),
    path('', bienvenida, name='bienvenida')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
