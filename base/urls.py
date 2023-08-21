from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_task_status/', views.check_task_status, name='check_task_status'),
]
