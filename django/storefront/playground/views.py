from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request -> Response
# Request Handler
# Action
# What users see

def say_hello(request):
    return HttpResponse('Hello World')