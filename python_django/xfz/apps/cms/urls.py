from django.urls import path,re_path
from . import views
app_name = 'csm'
urlpatterns = [
    path('login/', views.login_view, name='login'),
]