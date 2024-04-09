from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import EmailValidator, RegexValidator
import re
from core.utils import user_image_path
from .managers import UserManager
from core.models import BaseModel

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model representing a registered user in the system.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        phone_number (str): The phone number of the user, must be unique and 11 digits long.
        email (str): The email address of the user, must be unique and valid.
        image (str): The profile image of the user.
        role (str): The role of the user, chosen from predefined choices.
        created_at (datetime): The date and time when the user account was created.
        updated_at (datetime): The date and time when the user account was last updated.
        is_deleted (bool): Indicates whether the user account is deleted or not.
        deleted_at (datetime): The date and time when the user account was deleted.
        is_active (bool): Indicates whether the user account is active or not.
        is_admin (bool): Indicates whether the user has administrative privileges.
        objects (UserManager): The custom user manager for the user model.
    """

    # Choices for user roles
    ROLE_CHOICES = (
        ("Product Manager", "Product Manager"),
        ("Supervisor", "Supervisor"),
        ("Operator", "Operator"),
        ("Customer", "Customer"),
    ) 

    # Model fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11, unique=True, validators=[RegexValidator(r'^\d{11}$', message='Enter a valid 11-digit phone number.')])
    email = models.EmailField(max_length=255, validators=[EmailValidator(message='Enter a valid email address.')])
    image = models.ImageField(upload_to=user_image_path, null=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default="Customer")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def convert_to_english_numbers(self, input_str):
        """
        Convert Persian numbers in the given string to English numbers.

        Args:
            input_str (str): The input string possibly containing Persian numbers.

        Returns:
            str: The input string with Persian numbers converted to English numbers.
        """
        persian_to_english = {
            '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
            '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
        }
        persian_pattern = re.compile(r'[۰-۹]')
        english_number_str = persian_pattern.sub(lambda x: persian_to_english[x.group()], input_str)
        return english_number_str

    def clean_phone(self, phone_number):
        """
        Clean and validate the phone number.

        Args:
            phone_number (str): The phone number to be cleaned and validated.

        Returns:
            str: The cleaned and validated phone number.

        Raises:
            ValueError: If the phone number does not meet the required criteria.
        """
        cleaned_phone_number = self.convert_to_english_numbers(phone_number)
        if len(cleaned_phone_number) != 11:
            raise ValueError('Phone number should be 11 digits long.')
        return cleaned_phone_number

    def save(self, *args, **kwargs):
        self.phone_number = self.clean_phone(self.phone_number)
        super().save(*args, **kwargs)

    def delete(self):
        """
        Soft delete the user account.
        """
        self.is_deleted = True
        self.save()

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
            str: The email address of the user.
        """
        return self.email

    @property
    def is_staff(self):
        """
        Check if the user is staff (admin).

        Returns:
            bool: True if the user is staff (admin), False otherwise.
        """
        return self.is_admin

class Address(BaseModel):
    """
    Model representing a user address.

    Attributes:
        province (str): The province of the address.
        city (str): The city of the address.
        detailed_address (str): The detailed address information.
        postal_code (int): The postal code of the address.
        user (User): The user associated with this address.
    """
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    detailed_address = models.TextField()
    postal_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT , null=True , blank=True)
    
class OTPCODE(models.Model):
    """
    Model representing a one-time password (OTP) for user authentication.

    Attributes:
        phone_number (str): The phone number to which the OTP is sent.
        code (int): The OTP code.
        created (datetime): The date and time when the OTP was created.
    """
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the OTP object.

        Returns:
            str: A string containing phone number, OTP code, and creation date.
        """
        return f"{self.phone_number} - {self.code} - {self.created}"
