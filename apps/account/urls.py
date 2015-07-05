# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .resources import (
    UserViewSet,
)

router = DefaultRouter()
router.register(r'account', UserViewSet)

urlpatterns = patterns('',                         
)
urlpatterns += router.urls