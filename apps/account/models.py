from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Signasl Callbacks
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        Here when a user is create we create a Token for this user.
    """
    if created:
        Token.objects.create(user=instance)


   
from custom_user.models import AbstractEmailUser
class CustomUser(AbstractEmailUser):
    """
    Example of an EmailUser with a new field date_of_birth
    """
    date_of_birth = models.DateField(null=True, blank=True)    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


