from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def define(request):
    return HttpResponse('<h1>Python is high-level,opensource,interpreted,dynamic typed scripting language</h1>')
