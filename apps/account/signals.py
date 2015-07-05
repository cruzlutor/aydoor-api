# -*- coding: utf-8 -*-
from rest_framework.authtoken.models import Token


def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
        Here when a user is create we create a Token for this user.
    """
    if created:
        Token.objects.create(user=instance)