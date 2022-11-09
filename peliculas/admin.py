from django.contrib import admin

# Register your models here.
from .models import Director, Genero, Pelicula, PeliculaInstance

admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(PeliculaInstance)
