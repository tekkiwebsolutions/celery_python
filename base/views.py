from django.shortcuts import render
from .tasks import heavy_task
from django.http import JsonResponse


def index(request):
    heavy_task.delay()
    return JsonResponse({'status': 'ok'})
