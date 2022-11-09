from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>', views.DirectorView.as_view(), name='detalle_director'),
  path('pelicula/<int:pk>', views.PeliculaView.as_view(), name='detalle_pelicula'),

]