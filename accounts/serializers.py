from rest_framework import serializers
from .models import User,Address
from django.contrib import messages
from django.shortcuts import redirect
from product.serializers import UserSerializer
import re
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework.serializers import ModelSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "email", "password"]
    
    
    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value):
            raise serializers.ValidationError("This phone number is already in use")
        elif len(value) < 11:
            raise serializers.ValidationError("Your phone number is not correct. Must be 11 digits long")
        return value
        
    
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():  
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")
        return value
        
class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()
        
# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["email", "password"]

#     def validate_email(self, value):
#         # Custom email validation logic
#         if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
#             raise serializers.ValidationError("Invalid email format")
#         return value

#     def validate_password(self, value):
#         # Add custom password validation logic here
#         # For example, you can check if the password meets certain criteria
#         if len(value) < 6:
#             raise serializers.ValidationError("Password must be at least 6 characters long")
#         return value
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class OtpCodeSerializer(serializers.Serializer):
    code = serializers.CharField()
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','phone_number','email','first_name','last_name','image']
        


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'phone_number', 'email', 'password','first_name','last_name']
        
class AddressSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Address
        fields='__all__'