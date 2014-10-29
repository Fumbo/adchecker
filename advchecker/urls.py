from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from views import HomeView
from testapp.views import TestView


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view()),
                       url(r'^campagnes/', include('campagnes.urls')),
                       url(r'^tests/', TestView.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', auth_views.login),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
