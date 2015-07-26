from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello world and welcome to EchoBlue.')