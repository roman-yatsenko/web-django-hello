from datetime import datetime

from django.shortcuts import render

# Create your views here.


def index(request):
    now = datetime.today()
    return render(request, 'lection/index.html', context={
        'lection': now.weekday() == 0,
    })
