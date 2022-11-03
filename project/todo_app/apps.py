import imp
from django.apps import AppConfig

from django.core.signals import request_finished

class TodoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'

    # def ready(self) -> None:
        # from .todo_signal import post_save_todo
        # request_finished.connect(post_save_todo)

