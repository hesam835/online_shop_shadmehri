from rest_framework import serializers
from .models import User, Address
import re
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from product.serializers import UserSerializer
class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.

    This serializer handles the validation and creation of a new user instance.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        phone_number (str): The user's phone number.
        email (str): The user's email address.
        password (str): The user's password.
    """

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone_number", "email", "password"]
    
    def validate_phone_number(self, value):
        """
        Validate the phone number format and uniqueness.

        Args:
            value (str): The phone number to validate.

        Returns:
            str: The validated phone number.

        Raises:
            serializers.ValidationError: If the phone number is not in the correct format or is already in use.
        """
        if User.objects.filter(phone_number=value):
            raise serializers.ValidationError("This phone number is already in use")
        elif len(value) < 11:
            raise serializers.ValidationError("Your phone number is not correct. Must be 11 digits long")
        return value
    
    def validate_email(self, value):
        """
        Validate the email address uniqueness.

        Args:
            value (str): The email address to validate.

        Returns:
            str: The validated email address.

        Raises:
            serializers.ValidationError: If the email address is already in use.
        """
        if User.objects.filter(email=value).exists():  
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_password(self, value):
        """
        Validate the password length.

        Args:
            value (str): The password to validate.

        Returns:
            str: The validated password.

        Raises:
            serializers.ValidationError: If the password is less than 6 characters long.
        """
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long")
        return value

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.

    This serializer handles the validation of user login credentials.

    Attributes:
        phone_number (str): The user's phone number.
        password (str): The user's password.
    """

    phone_number = serializers.CharField()
    password = serializers.CharField()

class TokenRefreshSerializer(serializers.Serializer):
    """
    Serializer for token refresh.

    This serializer handles the validation of token refresh requests.

    Attributes:
        refresh (str): The refresh token.
    """

    refresh = serializers.CharField()

class OtpCodeSerializer(serializers.Serializer):
    """
    Serializer for OTP code validation.

    This serializer handles the validation of OTP codes.

    Attributes:
        code (str): The OTP code.
    """

    code = serializers.CharField()

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile details.

    This serializer handles the serialization of user profile details.

    Attributes:
        id (int): The user's ID.
        phone_number (str): The user's phone number.
        email (str): The user's email address.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        image (str): The URL of the user's profile image.
    """

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'first_name', 'last_name', 'image']

class UserCreateSerializer(BaseUserCreateSerializer):
    """
    Serializer for creating a new user.

    This serializer inherits from the Djoser's UserCreateSerializer and adds additional fields.

    Attributes:
        id (int): The user's ID.
        phone_number (str): The user's phone number.
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'phone_number', 'email', 'password', 'first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    """
    Serializer for user addresses.

    This serializer handles the serialization of user addresses.

    Attributes:
        user (UserSerializer): The serialized user object associated with the address.
    """

    user = UserSerializer()

    class Meta:
        model = Address
        fields = '__all__'
