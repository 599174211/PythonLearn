from django.urls import path,re_path,include
from . import views
app_name = 'manytomany'
urlpatterns = {
    path(r'', views.index, name ='index')
}