from django.views import generic

# Create your views here.
from .models import Director, Genero, Pelicula, PeliculaInstance

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Director

class DirectorView(generic.DetailView):
    template_name = 'director.html'
    model = Director

class PeliculaView(generic.DetailView):
    template_name = 'pelicula.html'
    model = Pelicula