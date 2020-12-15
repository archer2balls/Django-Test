from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, world. You're at the Blog!!!</h1>")

def members(request):
    return HttpResponse("<h1>Members Area Only</h1>")
