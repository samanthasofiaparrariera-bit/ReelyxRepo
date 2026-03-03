from .views.login_view import LoginView
from django.urls import path
from .views.register_view import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]