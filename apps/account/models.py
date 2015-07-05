from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver   
from custom_user.models import AbstractEmailUser
from .utils import upload_avatar
from .signals import create_auth_token

class CustomUser(AbstractEmailUser):
    """
    Example of an EmailUser with a new field date_of_birth
    """
    date_of_birth = models.DateField(null=True, blank=True)    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to=upload_avatar, null=True, blank=True)


post_save.connect(create_auth_token, sender=settings.AUTH_USER_MODEL)