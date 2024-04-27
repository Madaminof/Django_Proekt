from django.urls import path
from .views import get_info,get_name



urlpatterns=[
    path('app_url',get_info,name='app_url'),
    path('name', get_name, name='app_url'),

]