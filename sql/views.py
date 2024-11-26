from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def define(request):
    return HttpResponse('<h1>SQL is structured query language used to mainipulate the data in database</h1>')
