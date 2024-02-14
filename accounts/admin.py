from django.contrib import admin
from.models import User,Address,OTPCODE
from .forms import UserChangeForm,UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class User_display(admin.ModelAdmin):
    list_display = ("first_name","last_name","phone_number","email","role")
    
class RegisterAdress(admin.ModelAdmin):
    list_display = ("province","city")


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'phone_number','role','is_admin','first_name','last_name',)
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'first_name', 'last_name' ,'role' ,'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin','is_superuser','last_login','groups','user_permissions')}),
    )

    add_fieldsets = (
        (None, {'fields':('phone_number', 'email', 'first_name', 'last_name' ,'role','password1', 'password2')}),
    )
    search_fields = ('email', 'first_name')
    ordering = ('first_name',)
    filter_horizontal = ('groups','user_permissions')
    
    def __str__(self) -> str:
        return super().__str__()
    
@admin.register(OTPCODE)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number' , 'code' , 'created')
admin.site.register(User,UserAdmin)
admin.site.register(Address,RegisterAdress)