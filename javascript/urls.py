from django.urls import path
from javascript.views import *

urlpatterns = [
    path('define/',define,name='define'),
]