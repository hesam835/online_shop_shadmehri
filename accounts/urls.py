from django.urls import path
from .views import login,registerview,UserRegisterVerifyCodeView
urlpatterns = [
    path('login', login, name = 'login'),
    path('register', registerview.as_view(), name = 'register'),
    path("verify" , UserRegisterVerifyCodeView.as_view(),name="verify_code"),

]