"""HelloPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import serve,static
import os

urlpatterns = [
    path('admin/', admin.site.urls),

    # path(r'HelloPython2/', include('HelloPython2.urls',)),
    re_path(r'^HelloPython2/',include(('HelloPython2.urls', 'common'), namespace='python2')),
    re_path(r'BookManage/',include(('BookManage.urls','bookmanage'), namespace = 'book')),
    path(r'index/forpost', views.post_for),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
