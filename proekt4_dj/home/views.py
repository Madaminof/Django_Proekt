from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def get_photo(requests):
    return HttpResponse("<h1> Madaminov Samandar Backend developer</h1>")


def get_photo1(requests):
    return HttpResponse("<h1>Backend developer</h1>")

