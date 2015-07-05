# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from .resources import (
    ServiceViewSet, AdvertViewSet, BookingViewSet
)

router = DefaultRouter()

router.register(r'service', ServiceViewSet)
router.register(r'advert', AdvertViewSet)
router.register(r'booking', BookingViewSet)


urlpatterns = patterns('',                      
)
urlpatterns += router.urls