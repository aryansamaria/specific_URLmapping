from django.urls import path
from sql.views import *

urlpatterns = [
    path('define/',define,name='define'),
]