import datetime


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'hello/index.html')

def vlad(request):
    return HttpResponse('Hello, Vlad!')

def artem(request):
    return HttpResponse('Hello, Artem!')

def greet(request, name):
    return render(request, 'hello/greet.html', context={
        'name': name.capitalize(),
        'time': datetime.datetime.now(),
    })
