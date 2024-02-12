from django.urls import path
from .views import login,registerview
urlpatterns = [
    path('login', login, name = 'login'),
    path('register', registerview.as_view(), name = 'register'),
]