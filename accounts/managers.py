from django.contrib.auth.models import BaseUserManager
from django.db.models import Manager, QuerySet

class UserManager(BaseUserManager):
    """
    Custom user manager for the User model.

    This manager provides methods to create regular users and superusers.

    Attributes:
        BaseUserManager: Inherit from the BaseUserManager class provided by Django.
    """

    def create_user(self, phone_number, email, first_name, last_name, password):
        """
        Create a regular user.

        Args:
            phone_number (str): The user's phone number.
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            password (str): The user's password.

        Returns:
            User: The newly created user object.

        Raises:
            ValueError: If any of the required fields are missing.
        """
        if not phone_number:
            raise ValueError("User must have a phone number")

        if not email:
            raise ValueError("User must have an email")

        if not first_name:
            raise ValueError("User must have a first name")

        if not last_name:
            raise ValueError("User must have a last name")

        user = self.model( 
            phone_number=phone_number,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, email, first_name, last_name, password, address=None):
        """
        Create a superuser.

        Args:
            phone_number (str): The user's phone number.
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            password (str): The user's password.
            address (str): The user's address.

        Returns:
            User: The newly created superuser object.
        """
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        """
        Get the queryset for the User model.

        Returns:
            QuerySet: QuerySet containing all non-deleted user objects.
        """
        return QuerySet(self.model, using=self._db).exclude(is_deleted=True)
