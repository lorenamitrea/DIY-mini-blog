from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add_board/', views.add_board, name='add_board')
]