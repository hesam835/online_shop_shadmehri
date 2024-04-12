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
from .serializers import UserLoginSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.cache import cache_page

# redis
redis_client = redis.StrictRedis(host='redis', port=settings.REDIS_PORT, db=settings.REDIS_DB)


class UserRegisterView(View):
    """
    View for rendering the user registration form.

    Methods:
        get(request): Renders the user registration form.
    """
    def get(self, request):
        print("###########################################")
        return render(request, "register.html", {})


class UserRegisterAPIView(APIView):
    """
    API view for user registration.

    Methods:
        post(request): Handles POST request for user registration.
    """
    permission_classes = [AllowAny, ]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            random_code = random.randint(1000, 9999)
            print("##########################")
            print(random_code)
            send_otp_email(serializer.validated_data["email"], random_code)
            redis_client.setex(serializer.validated_data["email"], 180, random_code)
            email = serializer.validated_data["email"]
            hidden_email = email[:6] + '*'*(len(email)-20) + email[-14:]
            request.session["user_profile_info"] = {
                "first_name":serializer.validated_data["first_name"],
                "last_name":serializer.validated_data["last_name"],
                "phone_number":serializer.validated_data["phone_number"],
                "email":serializer.validated_data["email"],
                "password":serializer.validated_data["password"]
            }
            messages.success(request, f"we sent {hidden_email} a code", 'success')
            return redirect('verify_code')
        error_messages = serializer.errors
        for k, v in error_messages.items():
            message = v[0]
        messages.error(request, f"{message}", "danger")  
        return redirect('register')


class VerifyCodeView(View):
    """
    View for rendering the OTP verification form.

    Methods:
        get(request): Renders the OTP verification form.
    """
    def get(self, request):
        return render(request, "verify_code.html", {})


class VerifyCodeAPIView(APIView): 
    """
    API view for OTP verification.

    Methods:
        post(request): Handles POST request for OTP verification.
    """
    serializer_class=OtpCodeSerializer
    def post(self, request):
        try:
            email = request.session["user_profile_info"]["email"]
        except KeyError:
            return Response({"error": "Please register again"},status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            code = serializer.validated_data.get("code")
            if code == redis_client.get(email).decode('utf-8'):
                user_info = request.session.get("user_profile_info")
                try:
                    User.objects.create_user(
                        first_name=user_info["first_name"],
                        last_name=user_info["last_name"],
                        phone_number=user_info["phone_number"],
                        email=user_info["email"],
                        password=user_info["password"],
                    )
                    request.session.clear()
                    return Response(
                        {"message": "You are registered successfully",
                            "redirect_url": reverse("accounts:user_login")},
                        status=status.HTTP_200_OK
                    )
                except Exception as e:
                    return Response(
                        {"error": "Failed to register user", "detail": str(e)},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {"error": "Incorrect code"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"error": "Invalid input data"},
                status=status.HTTP_400_BAD_REQUEST
            )

def send_otp_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is: {otp}'
    from_email = 'shadmehrihesam@gmail.com'
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

def login(request):
    return render(request,"login.html",context={})


def customer_panel(request):
    return render(request,'customer_panel.html',context={})


def profile(request):
    return render(request,'profile.html',context={})


def add_address(request):
    return render(request,'add_address.html',context={})


def edit_profile(request):
    return render(request , 'edit_profile.html' , context={})


def edit_address(request,address_id):
    return render(request , 'edit_address.html' , context={})


def show_address(request):
    return render(request , 'address.html' , context={})


class ProfileAPiVIew(APIView):
    """
    API view for retrieving user profile details.

    Methods:
        get(request): Retrieves user profile details.
    """
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset=User.objects.get(id=request.user.id)
        serializer=ProfileSerializer(queryset)
        return Response({'queryset': serializer.data})


class UpdateAddressAPIView(APIView):
    """
    API view for updating user address.

    Methods:
        post(request): Handles POST request for updating user address.
    """
    permission_classes = [IsAuthenticated]
    def put(self, request,address_id):
        address=Address.objects.get(id=address_id)
        user_ser = AddressSerializer(address, data=request.data, partial=True)
        if user_ser.is_valid():
            user_ser.save()
        else:
            return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        redirect_url = reverse("customer_panel")  
        return Response({'redirect_url': redirect_url}, status=status.HTTP_200_OK)


class AddAddressAPIView(APIView):
    """
    API view for adding user address.

    Methods:
        post(request): Handles POST request for adding user address.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data=request.data
        address=Address.objects.create(province=data['province'],city=data['city'],detailed_address=data['detailed_address'],postal_code=data['postal_code'],user=request.user)
        return redirect('profile')


class UpdateProfileAPIView(APIView):
    """
    API view for updating user profile.

    Methods:
        get(request): Retrieves user profile and address details.
        put(request): Handles PUT request for updating user profile.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_ser = UserSerializer(instance=request.user)

        responses_data = {
            "customer_info":user_ser.data,
        }

        return Response(data=responses_data, status=status.HTTP_200_OK)

    def put(self, request):
        user_ser = UserSerializer(instance=request.user, data=request.data, partial=True)
        if user_ser.is_valid():
            user_ser.save()
        else:
            return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        redirect_url = reverse("customer_panel")  
        return Response({'redirect_url': redirect_url}, status=status.HTTP_200_OK)

from django.core.mail import send_mail
from django.http import HttpResponse

def email_form(request):
    return render(request, 'email_form.html')

