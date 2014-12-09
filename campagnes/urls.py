from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url

from campagnes.views import CampagnesAll, CampagnesDetail, CampagnesNew, ScreenshotsView


urlpatterns = patterns('',
                       url(r'^$', login_required(CampagnesAll.as_view()), name='index'),
                       url(r'^(?P<campagne_id>\d+)/$', login_required(CampagnesDetail.as_view()), name='detail'),
                       url(r'^new/$', login_required(CampagnesNew.as_view()), name='new'),
                       url(r'^screenshots/$', login_required(ScreenshotsView.as_view()), name='screenshots')
)
