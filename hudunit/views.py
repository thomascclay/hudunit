from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Susie")

def greeting(request):
    return HttpResponse("Greeting")

def lobby(request):
    #get all players
    pass

def brainstorm_question(request):
    pass

def answer_question(request):
    pass