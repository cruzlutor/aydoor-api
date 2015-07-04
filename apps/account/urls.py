# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from rest_framework.authtoken import views


urlpatterns = patterns('',      
    url(r'^api-token-auth/', views.obtain_auth_token)
)