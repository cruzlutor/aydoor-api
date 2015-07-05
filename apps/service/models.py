from django.db import models
from apps.account.models import CustomUser


class Service(models.Model):
    name = models.CharField(max_length=150)   
    advert = models.ManyToManyField(CustomUser, through='Advert', null=True, blank=True)
    # provider = models.ManyToManyField(CustomUser)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __unicode__(self):
        return '%s' % (self.name)


class Booking(models.Model):    
    price = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField()
    place =  models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __unicode__(self):
        return '%s' % (self.pk)


class Advert(models.Model):
    user = models.ForeignKey(CustomUser)
    service = models.ForeignKey(Service, related_name="service_advert")
    booking = models.ForeignKey(Booking)


# class Booking(models.Model):

#     name = models.CharField(max_length=150)

#     class Meta:
#         verbose_name = "Service"
#         verbose_name_plural = "Services"

#     def __unicode__(self):
#         return '%s' % (self.name)