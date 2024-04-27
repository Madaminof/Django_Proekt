from .views import get_photo,get_photo1
from django.urls import path


urlpatterns=[
    path('txt1',get_photo,name='txt1'),
    path('txt2',get_photo1,name='txt2')
]