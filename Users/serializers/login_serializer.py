from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise serializers.ValidationError("Email o contraseña incorrecta")
        else:
            raise serializers.ValidationError("Tienes que enviar el email y la contraseña")


        refresh = RefreshToken.for_user(user)

        return {'success': True,
                'data':{
                    'email': user.email,
                    'nombre': user.nombre,

                    'token': str(refresh.access_token),
                    'refreshToken': str(refresh),
                }


        }
