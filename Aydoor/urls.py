from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('apps.account.urls')),
    url(r'^api/', include('apps.service.urls')),
)

