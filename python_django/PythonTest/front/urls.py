from django.urls import include,path,re_path
from . import views
urlpatterns = {
    path(r'index/',views.index, name='index'),
}