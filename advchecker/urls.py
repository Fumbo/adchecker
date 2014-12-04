from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from advchecker.views import HomeView


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='index'),
                       url(r'^campagnes/', include('campagnes.urls', namespace="campagnes")),
                       url(r'^accounts/', include('accounts.urls', namespace="accounts")),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^conditions/', TemplateView.as_view(template_name="advchecker/docs.html"), name='docs'),
)
