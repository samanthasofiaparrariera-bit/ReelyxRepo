from django.contrib.auth.views import LoginView
from django.urls import path
from Users.views.register_view import RegisterView

urlpatterns = [
    path('registro/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]