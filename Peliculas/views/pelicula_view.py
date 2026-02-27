from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..model.pelicula_model import Pelicula
from Peliculas.serializers import PeliculaSerializer

class PeliculaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        peliculas = Pelicula.objects.all()
        serializer = PeliculaSerializer(peliculas, many=True)
        data = [{
            "name": pelicula.name,
            "year" : pelicula.year,
            "genre" : pelicula.genre,
            "duration" : pelicula.duration,
            "rating" : pelicula.rating,
        }
        for pelicula in peliculas]

        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)
