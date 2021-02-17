from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'registration/login.html')  # site login


def index(request):
    return HttpResponse(request)


def logout(request):
    return render(request, 'registration/logout.html')
