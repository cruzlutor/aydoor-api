from django.contrib import admin
from .models import Service, Booking, Advert


# class CustomUserAdmin(EmailUserAdmin):
#     """
#     You can customize the interface of your model here.
#     """
#     pass

# # Register your models here.
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Advert)