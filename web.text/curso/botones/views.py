from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the botones index.")


def b(request):
    return render(request, 'templates/test.html')
