from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    oge_link = 'oge/'
    link_html_text = f'<a href="{oge_link}">OGE</a>'
    return HttpResponse(link_html_text)
