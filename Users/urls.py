from django.contrib.auth.views import LoginView
from django.urls import path
from .views.register_view import RegisterView


urlpatterns = [
    path('registro/', RegisterView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
]