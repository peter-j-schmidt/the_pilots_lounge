from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return HttpResponse("Hello, world. You're at the users index.")

def detail(request, user_id):
    return HttpResponse("You are looking at user %s." % user_id)

def results(request, user_id):
    response = "You're looking at the info of user %s."
    return HttpResponse(response % user_id)