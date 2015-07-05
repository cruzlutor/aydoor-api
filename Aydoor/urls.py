from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    # (r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('apps.account.urls')),
    url(r'^api/', include('apps.service.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

