from django.db import models

# Create your models here.
class Partido(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Candidato(models.Model):
    nombre = models.CharField(max_length=250)
    apellido_pat = models.CharField(max_length=250)
    apellido_mat = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to="fotos", null=True, blank=True)
    partido = models.ForeignKey('votacion.Partido', verbose_name='Partido', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido_pat} {self.apellido_mat}"

class Votacion(models.Model):
    candidato = models.ForeignKey('votacion.Candidato', verbose_name='Candidato', on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()