from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('vlad', views.vlad, name='vlad'),
    path('artem', views.artem, name='artem'),
    path('<str:name>', views.greet, name='greet'),
]
