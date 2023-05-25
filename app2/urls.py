from django.urls import path
from app2.views import *

app_name = 'app2'

urlpatterns = [
    path('app2_string1/',app2_string1,name='app2_string1'),
    path('app2_string2/',app2_string2,name='app2_string2'),
]