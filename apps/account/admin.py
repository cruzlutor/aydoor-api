from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import CustomUser


class CustomUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    pass

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)