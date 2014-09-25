from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'advchecker.views.home', name='home'),

                       url(r'^auchan/', include('auchan.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
