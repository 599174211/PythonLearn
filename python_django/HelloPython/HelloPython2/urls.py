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
from django.urls import path,re_path
from . import views
urlpatterns = [
    path(r'index/',views.index, name = 'index'),
    path(r'index1/', views.index1, name='index1'),
    path(r'index/request',views.request_item, name = 'requet.item'),
    path(r'index/forpost', views.for_post, name ='for_post'),
    path(r'index/<int:number>', views.index2, name='index2'),
    re_path(r'^index/(?:page-(?P<pg>\d+))',views.page, name='page'),
    path(r'index/aaa', views.index3, name='index3'),
    path(r'index/exception', views.exception, name='exception'),
    path(r'index/render', views.forrender, name = 'forrender'),
    path(r'index/render1', views.forrender1, name = 'forrender1'),
    path(r'index/render2', views.forrender2, name = 'forrender2'),
    path(r'index/for404', views.for404, name='for404'),
    path(r'index/extends_1', views.extends_1,name = 'extends_1'),
    path(r'index/base', views.base, name = 'base'),
    path(r'index/base/company', views.company, name = 'company'),
    path(r'index/base/school', views.school, name = 'school'),
]
