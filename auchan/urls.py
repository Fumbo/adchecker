from django.conf.urls import patterns, url

from auchan import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<drive_id>\d+)/$', views.detail, name='detail'),
                       )
