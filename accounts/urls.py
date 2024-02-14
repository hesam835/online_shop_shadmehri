from django.urls import path
from .views import login,VerifyCodeAPIView,UserRegisterView,VerifyCodeView,UserRegisterAPIView
urlpatterns = [
    path('login', login, name = 'login'),
    path('register', UserRegisterView.as_view(), name = 'register'),
    path("verify_code" , VerifyCodeView.as_view(),name="verify_code"),
    path("api/register/", UserRegisterAPIView.as_view(), name="user_register_api"),
    path("api/verify/", VerifyCodeAPIView.as_view(), name="verify_code_api"),
]