from django.urls import path
from .consumers import TaskStatusConsumer

websocket_urlpatterns = [
    path('ws/task_status/<str:task_id>/', TaskStatusConsumer.as_asgi()),
    # path('ws/task_status/', TaskStatusConsumer.as_asgi()),

]
