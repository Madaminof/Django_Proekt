from django.urls import path
from .views import index,home





urlpatterns=[
    path('function',index,name='func2'),
    path('html',home,name='html')

]