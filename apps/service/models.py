from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __unicode__(self):
        return '%s' % (self.name)
