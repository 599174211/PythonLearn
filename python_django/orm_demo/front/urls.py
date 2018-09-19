from django.urls import path,re_path
from . import views
app_name = 'front'
urlpatterns = {
    path(r'', views.index, name='index'),
    path(r'index1/', views.index1, name='index1'),
    path(r'index2/', views.index2, name='index2'),
    path(r'index3/', views.index3, name='index3'),
    path(r'index4/', views.index4, name='index4'),
    path(r'index5/', views.index5, name='index5'),
    path(r'index6/', views.index6, name='index6'),
    path(r'index7/', views.index7, name='index7'),
    path(r'index8/', views.index8, name='index8'),
    path(r'index9/', views.index9, name='index9'),
    path(r'index10/', views.index10, name='index10'),
    path(r'index11/', views.index11, name='index11'),
    path(r'index12/', views.index12, name='index12'),
    path(r'index13/', views.index13, name='index13'),
    path(r'index14/', views.index14, name='index14'),
}