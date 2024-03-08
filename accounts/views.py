from django.shortcuts import render, redirect
from django.views import View
from product.serializers import UserSerializer
from .serializers import UserRegisterSerializer, OtpCodeSerializer , UserLoginSerializer,ProfileSerializer,AddressSerializer
from .models import User,Address
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions,status
import random
from utils import send_otp_code
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from rest_framework.permissions import AllowAny
from django.conf import settings
import redis
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from .serializers import LoginSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.cache import cache_page

# redis
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


class UserRegisterView(View):
    def get(self, request):
        return render(request, "register.html", {})
    

class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.POST)
        if serializer.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(serializer.validated_data["phone_number"], random_code)
            # OtpCode.objects.create(phone_number=serializer.validated_data["phone_number"], code=random_code)
            redis_client.setex(serializer.validated_data["phone_number"], 180, random_code)
            phone_number = serializer.validated_data["phone_number"]
            hidden_phone_number = phone_number[:2] + '*'*(len(phone_number)-4) + phone_number[-2:]
            request.session["user_profile_info"] = {
                "first_name":serializer.validated_data["first_name"],
                "last_name":serializer.validated_data["last_name"],
                "phone_number":serializer.validated_data["phone_number"],
                "email":serializer.validated_data["email"],
                "password":serializer.validated_data["password"]
            }
            messages.success(request, f"we sent {hidden_phone_number} a code", 'success')
            return redirect('verify_code')
        error_messages = serializer.errors
        for k, v in error_messages.items():
            message = v[0]
        messages.error(request, f"{message}", "danger")  
        return redirect('register')
    
class VerifyCodeView(View):
     def get(self, request):
        return render(request, "verify_code.html", {})

        
def login(request):
    return render(request,"login.html",context={})

class VerifyCodeAPIView(APIView): 
    def post(self, request):
        if "user_profile_info" not in request.session or "phone_number" not in request.session["user_profile_info"]:
            messages.error(request, "Please register again", "danger")
            return redirect("register")
            
        phone_number = request.session["user_profile_info"]["phone_number"]
        
        serializer = OtpCodeSerializer(data=request.POST)
        
        if serializer.is_valid():
            stored_code = redis_client.get(phone_number)
            if stored_code and stored_code.decode('utf-8') == serializer.validated_data["code"]:
                user_info = request.session["user_profile_info"]
                try:
                    User.objects.create_user(
                        first_name=user_info["first_name"],
                        last_name=user_info["last_name"],
                        phone_number=user_info["phone_number"],
                        email=user_info["email"],
                        password=user_info["password"],
                    )   
                    request.session.clear()
                    messages.success(request, "You registered successfully")
                    return redirect("login")
                except:
                    messages.error(request, "You are already registered", "danger")
                    return redirect("login")
            messages.error(request, "Code is not correct", "danger")
            return redirect("verify_code")
        return  redirect("login")
    
# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.data['user'] # This line needs to be changed
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def token_refresh(request):
#     serializer = TokenRefreshSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     refresh = RefreshToken(serializer.validated_data['refresh'])
#     return Response({
#         'access': str(refresh.access_token),
#     })
    
# class UserLoginAPIView(APIView):
#     permission_classes = []

#     def post(self, request):-
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             phone_number = serializer.validated_data["phone_number"]
#             password = serializer.validated_data["password"]

#             user = authenticate(phone_number=phone_number, password=password)

#             if user is not None:
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                 })
#             else:
#                 return Response({'error': 'Invalid username/password'}, status=400)

#         return Response(serializer.errors, status=400)
    
def customer_panel(request):
    return render(request,'customer_panel.html',context={})

def profile(request):
    return render(request,'profile.html',context={})

def edit_profile(request):
    return render(request , 'edit_profile.html' , context={})

def edit_address(request,address_id):
    return render(request , 'edit_address.html' , context={})

def show_address(request):
    return render(request , 'address.html' , context={})

#show profile detail in customer panel
class ProfileAPiVIew(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset=User.objects.get(id=request.user.id)
        serializer=ProfileSerializer(queryset)
        return Response({'queryset': serializer.data})
    
# edit address(province,city,address detail,postal code)   
class UpdateAddressAPIView(APIView):
    def post(self, request):
        data=request.data
        address=Address.objects.update(province=data['province'],city=data['city'],detailed_address=data['detailed_address'],postal_code=data['postal_code'],user=request.user)
        return redirect('profile')

# edit profile in customer
# class UpdateProfileAPIView(APIView):
#     def post(self, request):
#         data = request.data
#         phone_number = data.get('phone_number')
        
#         # Check if the phone number already exists
#         existing_user = User.objects.filter(phone_number=phone_number).first()
#         if existing_user:
#             # Update existing user
#             existing_user.first_name = data.get('first_name', existing_user.first_name)
#             existing_user.last_name = data.get('last_name', existing_user.last_name)
#             existing_user.email = data.get('email', existing_user.email)
#             existing_user.save()
#             return redirect('profile')
#         else:
#             # Create new user
#             profile = User.objects.create(
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 phone_number=phone_number,
#                 email=data['email']
#             )
#             return redirect('profile')


class UpdateProfileAPIView(APIView):
    def get(self, request):
        user_ser = UserSerializer(instance=request.user)
        addresses = Address.objects.filter(user=request.user)
        address_ser = AddressSerializer(instance=addresses, many=True)
        
        responses_data = {
            "customer_info":user_ser.data,
            "address_info":address_ser.data,
        }
        
        return Response(data=responses_data, status=status.HTTP_200_OK)
    
    def put(self, request):
        user_ser = UserSerializer(instance=request.user, data=request.data, partial=True)
        if user_ser.is_valid():
            user_ser.save()
        else:
            return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        redirect_url = reverse("accounts:user_panel")  
        return Response({'redirect_url': redirect_url}, status=status.HTTP_200_OK)


