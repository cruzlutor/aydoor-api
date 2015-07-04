from django.db import models

# Create your models here.
class Service(models.Model):

	

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __unicode__(self):
        pass
    