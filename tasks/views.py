from django.shortcuts import render

# Create your views here.

tasks = ['Web', 'Python', 'Django', 'Електронна комерція']

def index(request):
    return render(request, 'tasks/index.html', context={
        'tasks': tasks,
    })

def add(request):
    return render(request, 'tasks/add.html')
