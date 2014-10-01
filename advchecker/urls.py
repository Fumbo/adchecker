from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'advchecker.views.home', name='home'),

                       url(r'^campagnes/', include('campagnes.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
