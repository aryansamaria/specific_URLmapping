from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def define(request):
    return HttpResponse('<h1>Javascript is high-level language used to give dynamic functionality to the web page</h1>')
