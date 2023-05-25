from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_string1(request):
    return HttpResponse('<h1>This is app2_string1 response from app2</h1>')

def app2_string2(request):
    return HttpResponse('<h1>This is app2_string2 response from app2</h1>')