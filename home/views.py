from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def Home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def Hello(request):
    return HttpResponse("Hello world!")
