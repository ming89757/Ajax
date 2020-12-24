from django.conf.urls import url
from . import views

appname = 'ajax1'
urlpatterns = [
    url(r'^01-load/$', views.load_views),
    url(r'^01-server/$', views.server01),
    url(r'^02-get/$', views.get_views),
    url(r'^02-server/$', views.server02),
    url(r'^03-post/$', views.post_views),
    url(r'^03-server/$', views.server03),
    url(r'^04-ajax/$', views.ajax_views),
    url(r'^04-server/$', views.server04),
]
