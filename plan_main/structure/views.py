from django.http import HttpRequest
from django.shortcuts import render, HttpResponse


def index(request: HttpRequest):
    return HttpResponse(content='<h1>Hello world!</h1>')
