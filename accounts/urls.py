from django.urls import path
from .views import login,VerifyCodeAPIView,UserRegisterView,VerifyCodeView,UserRegisterAPIView,customer_panel,profile,ProfileAPiVIew,edit_profile
from order.views import ShowAddressApi
urlpatterns = [
    path('customer_panel',customer_panel , name = 'customer_panel'),
    path('profile', profile, name = 'profile'),
    path('login', login, name = 'login'),
    path('register', UserRegisterView.as_view(), name = 'register'),
    path("verify_code" , VerifyCodeView.as_view(),name="verify_code"),
    path("api/register/", UserRegisterAPIView.as_view(), name="user_register_api"),
    path("api/verify/", VerifyCodeAPIView.as_view(), name="verify_code_api"),
    path("api/profile/", ProfileAPiVIew.as_view(), name="profile_api"),
    path("api/address/", ShowAddressApi.as_view(), name="address_api"),
    path('edit_profile', edit_profile, name = 'edit_profile'),

]