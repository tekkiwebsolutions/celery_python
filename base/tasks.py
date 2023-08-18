from celery import shared_task
from time import sleep


@shared_task
def heavy_task():
    for i in range(7):
        sleep(1)
        print(i)
    return 'done'
