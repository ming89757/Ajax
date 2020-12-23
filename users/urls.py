from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.userindex),
    url(r'^chkname/', views.chkUname),
    url(r'^reguser/$', views.reguser),
]
