from django.urls import path
from .views import login,VerifyCodeAPIView,UserRegisterView,VerifyCodeView,UserRegisterAPIView,customer_panel,profile,ProfileAPiVIew,edit_profile,edit_address,UpdateAddressAPIView,UpdateProfileAPIView,show_address,add_address,AddAddressAPIView,email_form
from order.views import ShowAddressApi
urlpatterns = [
    path('customer_panel',customer_panel , name = 'customer_panel'),
    path('profile', profile, name = 'profile'),
    path('login', login, name = 'login'),
    path('register', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile', edit_profile, name = 'edit_profile'),
    path("verify_code" , VerifyCodeView.as_view(),name="verify_code"),
    path('edit_address/<int:address_id>', edit_address, name = 'edit_address'),
    path('show_address', show_address, name = 'show_address'), 
    path('add_address', add_address, name = 'add_address'),
    #==========api============
    path("api/register/", UserRegisterAPIView.as_view(), name="user_register_api"),
    path("api/verify/", VerifyCodeAPIView.as_view(), name="verify_code_api"),
    path("api/profile/", ProfileAPiVIew.as_view(), name="profile_api"),
    path("api/address/", ShowAddressApi.as_view(), name="address_api"),
    path("api/update_address/", UpdateAddressAPIView.as_view(), name="update_address_api"),
    path("api/update_profile/", UpdateProfileAPIView.as_view(), name="update_profile_api"),
    path("api/add_address/", AddAddressAPIView.as_view(), name="add_address_api"),

]