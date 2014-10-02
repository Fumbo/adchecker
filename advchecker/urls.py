from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'advchecker.views.index', name='index'),
                       url(r'^campagnes/', include('campagnes.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
