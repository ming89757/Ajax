"""Ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('users.urls')),
    url(r'^ajax1/', include('ajax1.urls')),
    url(r'^01-xhr', views.xhr01),
    url(r'^02-ajax1-get/$', views.ajax_get),
    url(r'^02-server$', views.server02),
    url(r'^02-server-param$', views.server02_param),
    url(r'^03-ajax1-post/$', views.ajax_post),
    url(r'^03-server/$', views.server03),
]
