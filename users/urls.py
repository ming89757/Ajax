from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userindex),
    url(r'^chkname/', views.chkUname),
    url(r'^reguser/$', views.reguser),
    url(r'^query/$', views.query_user),
    url(r'^query_server/$', views.query_server),
    url(r'^json/$', views.json_views),
    url(r'^json_server/$', views.json_server),
    url(r'^user_server/$', views.user_server),
    url(r'^front_json/$', views.front_json),
    url(r'^front_server/$', views.front_server),
]
