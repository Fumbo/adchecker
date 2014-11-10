from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from views import HomeView
from testapp.views import TestView


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view()),
                       url(r'^campagnes/', include('campagnes.urls')),
                       url(r'^accounts/', include('accounts.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^conditions/', TemplateView.as_view(template_name="advchecker/docs.html"), name='docs'),


                       url(r'^tests/', TestView.as_view()),
)
