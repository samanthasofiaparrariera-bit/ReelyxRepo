from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..model.listas_model import Lista

class ListasView(APIView):
    permission_classes = [AllowAny]



    def get(self, request):
        #dejo un is_active en caso de que alguien quiera archivar o eliminar una lista
        listas = Lista.objects.filter(is_active=True).order_by('id')
        data = [
            {
                "nombre": lista.nombre,
                "usuario": lista.usuario,
                "descripcion": lista.descripcion,
                "creado": lista.creado,
                "actualizado": lista.actualizado,
                "slug_lista": lista.slug,
                "cant_peliculas": lista.peliculas(lista),

            }
            for lista in listas
        ]

        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

