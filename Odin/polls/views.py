from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, response
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged.


# def index(request):
#     return HttpResponse("<h1>Hello, world. You're at the Polls!!!</h1>")

def members(request):
    return HttpResponse("<h1>Members Area Only</h1>")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)