from django.db import models
from apps.account.models import CustomUser


class Service(models.Model):
    name = models.CharField(max_length=150)   
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __unicode__(self):
        return '%s' % (self.name)


class Advert(models.Model):    
    service = models.ForeignKey(Service)
    user_provider = models.ForeignKey(CustomUser, related_name='provider_advert')
    booking = models.ManyToManyField(CustomUser, through='Booking', related_name='booking')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Advertices"

    def __unicode__(self):
        return '%s' % (self.pk)


class Booking   (models.Model):    

    REQUEST = 1
    ACCPETED = 2
    CANCELED = 3
    FINISHED = 4
    STATES_BOOKING = ( 
        (REQUEST, 'REQUEST'),
        (ACCPETED, 'ACCPETED'),
        (CANCELED, 'CANCELED'),
        (FINISHED, 'FINISHED')
    )

    user_client = models.ForeignKey(CustomUser, related_name='client_advert')
    advert = models.ForeignKey(Advert, related_name='advert_booking')

    price = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField()
    place =  models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    comments = models.TextField(null=True, blank=True)
    state = models.PositiveSmallIntegerField(default=1, max_length=1, choices=STATES_BOOKING)
    amount = models.PositiveSmallIntegerField(max_length=2)

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __unicode__(self):
        return '%s' % (self.pk)