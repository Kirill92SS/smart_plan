from django.shortcuts import render, HttpResponse


def index(req):
    return HttpResponse(content='<h1>Hello world!</h1>')
