from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_info(request):
    return HttpResponse('<h1>hello python<h1><hr/>')

def get_name(request):
    return HttpResponse('<h1>Madaminov Samandar<h1><hr/>')

