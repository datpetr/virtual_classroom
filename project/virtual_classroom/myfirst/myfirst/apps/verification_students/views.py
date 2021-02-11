from django.http import HttpResponse


def index(request):
    return HttpResponse('Hi, world!!!')


def test(request):
    return HttpResponse('it is test')
