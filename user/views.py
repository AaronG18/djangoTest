from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is userIndex')


def userLogin(request):
    return HttpResponse('This is userLogin')
