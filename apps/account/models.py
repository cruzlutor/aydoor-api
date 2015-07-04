from django.db import models
from django.contrib.auth.models import User


class User(models.Model):

	auth_user = models.ForeignKey(User)
	

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        pass
    