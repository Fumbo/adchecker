from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url

from views import CampagnesAll, CampagnesDetail


urlpatterns = patterns('',
                       url(r'^$', login_required(CampagnesAll.as_view()), name='index'),
                       url(r'^(?P<campagne_id>\d+)/$', login_required(CampagnesDetail.as_view()), name='detail'),
)
