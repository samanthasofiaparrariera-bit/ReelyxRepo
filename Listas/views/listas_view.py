from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import CustomUser
from ..model.listas_model import Lista
from ..serializers.listas_serializers import ListaSerializer
from rest_framework.permissions import IsAuthenticated

class ListasView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("USER:", request.user)
        print("IS AUTH:", request.user.is_authenticated)

        serializer = ListaSerializer(data=request.data)

        if serializer.is_valid():
            lista = serializer.save(usuario=request.user)
            return Response({"success": True, "data": lista}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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
                "cant_peliculas": lista.numPelis(),

            }
            for lista in listas
        ]

        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

