from rest_framework import serializers
from Peliculas.model.pelicula_model import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'
