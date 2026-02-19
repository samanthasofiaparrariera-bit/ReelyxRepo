from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)


            data = {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_slug": user.username,
                "is_staff": user.is_staff
            }

            return Response({"data": data, "Bienvenido": True}, status=status.HTTP_200_OK)

        else:
            return Response(
                {"data": "Usuario o contraseña incorrectos", "Bienvenido": False},
                status=status.HTTP_401_UNAUTHORIZED
            )