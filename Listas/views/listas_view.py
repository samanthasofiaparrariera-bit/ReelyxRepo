from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..model.listas_model import Lista

class ListasView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        lists = Lista.objects.filter(is_active=True).order_by('id', '-name')

        data = [{
            "nombre": lists.name,
            "usuario": lists.usuario,
            "descripcion": lists.descripcion,
            "creado": lists.creado,
            "actualizado": lists.actualizado,
            "slug_lista": lists.slug_lista,

        }]

