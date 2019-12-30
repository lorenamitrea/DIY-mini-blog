from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('add_board/', views.add_board, name='add_board'),
    path('add_task/<int:pk>/', views.add_task, name='add_task'),
    path('check/<int:pk>/', views.check, name='check'),
    path('delete_board/<int:pk>/', views.delete_board, name='delete_board')
]
