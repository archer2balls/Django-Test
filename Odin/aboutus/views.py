from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.



def index(request):
    curDT = datetime.now()
    date_time = curDT.strftime("%d/%m/%Y, %H:%M:%S") # Can set date it as m/d/Y also
    return render(request,"aboutus/index.html",{"datetime":date_time})
    #return HttpResponse("<h1>Hello, world. This is ABOUT US!!!</h1>")


def aboutus(request):
    return HttpResponse("<h1>Hello, world. This is about us!!!</h1>")