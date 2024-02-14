from django.shortcuts import render, redirect
from django.views import View
from .serializers import UserRegisterSerializer, OtpCodeSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import random
from utils import send_otp_code
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from rest_framework.permissions import AllowAny
from django.conf import settings
import redis

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
            print("************************************************************")
            print(request.session["user_profile_info"] )
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
        return redirect("login")