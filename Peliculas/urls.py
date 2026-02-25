from django.urls import path
from .views.pelicula_view import PeliculaView


urlpatterns = [
    # path('lista/', views.a, name='a'),
    path("", PeliculaView.as_view(), name = "Peliculas"),

]