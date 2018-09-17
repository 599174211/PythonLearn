from  django.urls import path,re_path
from . import views
app_name = 'orm'
urlpatterns = [
    path('index/',views.index, name = 'index'),
]