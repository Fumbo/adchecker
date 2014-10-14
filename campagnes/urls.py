from django.conf.urls import patterns, url

from views import CampagnesAll, CampagnesDetail

urlpatterns = patterns('',
                       url(r'^$', CampagnesAll.as_view(), name='index'),
                       url(r'^(?P<campagne_id>\d+)/$', CampagnesDetail.as_view(), name='detail'),
                       )
