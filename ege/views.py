from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/ege">http://127.0.0.1:8000/ege</a>')