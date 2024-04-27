from .views import project1,project2
from django.urls import path
urlpatterns=[
    path('proekt1',project1,name='proekt1'),
    path('proekt2',project2,name='proekt2')
]