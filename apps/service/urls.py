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
    # url(r'^cooperative/module/$', CooperativeModuleResource.as_view()),
    # url(r'^cooperative/state/(?P<pk>[0-9]+)/$', CooperativeCreationByExisting.as_view()),
)
urlpatterns += router.urls