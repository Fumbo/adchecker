from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from accounts.views import Register


urlpatterns = patterns('',
                       url(r'^login/$', auth_views.login, name='login'),
                       url(r'^logout/$', auth_views.logout_then_login, name='logout'),
                       url(r'^signup/$', Register.as_view(), name="signup"),
)
