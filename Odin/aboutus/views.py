from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world. This is ABOUT US!!!</h1>")

def aboutus(request):
    return HttpResponse("<h1>Hello, world. This is about us!!!</h1>")