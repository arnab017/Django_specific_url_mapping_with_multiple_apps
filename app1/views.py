from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_string1(request):
    return HttpResponse('<h1>this is app1_string1 response from app1</h1>')

def app1_string2(request):
    return HttpResponse('<h1>this is app1_string2 response from app1</h1>')