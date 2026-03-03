from rest_framework import serializers
from Listas.model import Lista
from Peliculas.model import Pelicula


class ListaSerializer(serializers.ModelSerializer):

    peliculas = serializers.ListField(child=serializers.IntegerField(),allow_empty=False)

    class Meta:
        model = Lista
        fields = ('nombre','descripcion','peliculas')
    # esta función se asegura de que no hay más de 30 películas.
    def validar_peliculas(self,peliculas_ids):

        peliculas_ids = list(dict.fromkeys(peliculas_ids))
        if len(peliculas_ids)>30:
            raise serializers.ValidationError("No se puede añadir más de 30 películas")


        existen = Pelicula.objects.filter(id__in=peliculas_ids).values_list('id',flat=True)
        faltan = set(peliculas_ids)-set(existen)
        if faltan:
            raise serializers.ValidationError(f"Películas no encontradas: {list(faltan)}")
        return peliculas_ids

    def create(self,validated_data):

        usuario = validated_data.pop('usuario')
        peliculas_ids = validated_data.pop('peliculas')

        lista = Lista.objects.create(
            usuario=usuario,
            nombre=validated_data['nombre'],
            descripcion=validated_data.get('descripcion',''),
        )
        pelis = Pelicula.objects.filter(id__in=peliculas_ids)
        lista.peliculas.set(pelis)

        return lista