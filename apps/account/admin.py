from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _

class CustomUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    # fields = ( 'date_of_birth', 'first_name', 'last_name', 'city', 'avatar', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'city', 'avatar', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)