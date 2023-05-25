from django.urls import path
from app1.views import *

app_name = 'app1'

urlpatterns = [
    path('app1_string1/',app1_string1,name='app1_string1'),
    path('app1_string2/',app1_string2,name='app1_string2'),
]
