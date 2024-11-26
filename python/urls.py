from django.urls import path
from python.views import *

urlpatterns = [
    path('define/',define,name='define'),
]