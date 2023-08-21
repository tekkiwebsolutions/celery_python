from django.shortcuts import render
from django.http import JsonResponse
from celery.result import AsyncResult
# from django_celery_results.models import TaskResult

from .tasks import heavy_task


def index(request):
    task_result = heavy_task.delay()
    context = {'task_id': task_result.task_id}
    return render(request, 'base/index.html', context)


def check_task_status(request):
    task_id = request.GET.get('task_id', None)
    response_data = {'status': 'No task found'}
    task_result = AsyncResult(task_id)
    if task_id and task_result:
        response_data = {
            'status': task_result.status, 'task_id': task_id,
            'result': task_result.result
        }
    return JsonResponse(response_data)
