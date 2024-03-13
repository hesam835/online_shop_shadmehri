from django.contrib import admin
from .models import User, Address, OTPCODE
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class User_display(admin.ModelAdmin):
    """
    Customizes the display of user information in the admin panel.

    This admin model displays specific user fields in the admin panel.

    Attributes:
        list_display (tuple): The fields to be displayed in the list view of the admin panel.
    """
    list_display = ("first_name", "last_name", "phone_number", "email", "role")
    
class RegisterAdress(admin.ModelAdmin):
    """
    Customizes the display of address information in the admin panel.

    This admin model displays specific address fields in the admin panel.

    Attributes:
        list_display (tuple): The fields to be displayed in the list view of the admin panel.
    """
    list_display = ("province", "city")

class UserAdmin(BaseUserAdmin):
    """
    Customizes the user admin panel.

    This admin class provides customization for the user admin panel, including form settings, fieldsets,
    search functionality, and display options.

    Attributes:
        form (Form): The form used for updating user details.
        add_form (Form): The form used for creating new users.
        list_display (tuple): The fields to be displayed in the list view of the admin panel.
        list_filter (tuple): The fields to filter users in the admin panel.
        fieldsets (tuple): The fieldsets to organize user fields in the admin panel.
        add_fieldsets (tuple): The fieldsets to organize user fields when adding a new user in the admin panel.
        search_fields (tuple): The fields to be searched when using the search functionality in the admin panel.
        ordering (tuple): The fields used for ordering users in the admin panel.
        filter_horizontal (tuple): The fields to be displayed in a horizontal filter in the admin panel.

    Methods:
        __str__(): Returns the string representation of the admin class.
    """
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'phone_number', 'role', 'is_admin', 'first_name', 'last_name',)
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'first_name', 'last_name', 'role', 'password', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2', 'image')}),
    )
    search_fields = ('email', 'first_name')
    ordering = ('first_name',)
    filter_horizontal = ('groups', 'user_permissions')
    
    def __str__(self) -> str:
        """
        Returns the string representation of the admin class.

        Returns:
            str: The string representation of the admin class.
        """
        return super().__str__()

@admin.register(OTPCODE)
class OtpCodeAdmin(admin.ModelAdmin):
    """
    Customizes the display of OTP codes in the admin panel.

    This admin model displays OTP code details in the admin panel.

    Attributes:
        list_display (tuple): The fields to be displayed in the list view of the admin panel.
    """
    list_display = ('phone_number', 'code', 'created')

# Register the admin classes
admin.site.register(User, UserAdmin)
admin.site.register(Address, RegisterAdress)
