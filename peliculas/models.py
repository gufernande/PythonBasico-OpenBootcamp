from django.db import models
import uuid

# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del Genero")

    def __str__(self):
        return self.name

class Director(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    fechaNacimiento = models.DateField(null=True, blank=True)
    fechaFallecimiento = models.DateField('Died', null=True, blank=True)
    imagen = models.URLField(null=True, blank=True)
    biografia = models.TextField(max_length=200, help_text="Resumen biografia", null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Pelicula(models.Model):
    titulo = models.CharField(max_length=64)
    autor = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=200, help_text="Sinopsis de la palicula")
    genero = models.ManyToManyField(Genero)
    fecha = models.DateField(null=True, blank=True)
    duracion= models.CharField(max_length=5, null=True, blank=True, help_text="formato: hh:mm 01:58")
    imagen = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class PeliculaInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de pelicula")
    pelicula = models.ForeignKey('Pelicula', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.pelicula