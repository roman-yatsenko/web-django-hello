from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import NewTaskForm

# Create your views here.

tasks = ['Web', 'Python', 'Django', 'Електронна комерція']

def index(request):
    return render(request, 'tasks/index.html', context={
        'tasks': tasks,
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return redirect(reverse('index'))

    return render(request, 'tasks/add.html', context={
        'form': NewTaskForm(),
    })
