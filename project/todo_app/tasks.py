from celery import shared_task
from . import models
import time
@shared_task()
def send_email(pk):
    todo = models.Todo.objects.get(pk=pk)
    for i in range(0, 10):
        time.sleep(2)
        print("todo task " + todo.title)
