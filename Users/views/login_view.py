from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email') or request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)


            data = {
                "email": user.email,
                "nombre": user.nombre,
                "is_staff": user.is_staff
            }

            return Response({"data": data, "Bienvenido": True}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"data": "Usuario o contraseña incorrectos", "Bienvenido": False},
                status=status.HTTP_401_UNAUTHORIZED
            )