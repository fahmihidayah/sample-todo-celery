from django.shortcuts import render
from django.views import generic
from . import models
from django.core.cache import cache

# Create your views here.

class TodoListView(generic.ListView):
    model = models.Todo
    queryset = models.Todo.objects.all()

    # def get_queryset(self):
    #     result = cache.get('todos')
    #     print(result)
    #     if result is None:
    #         result = super(TodoListView, self).get_queryset()
    #         cache.set('todos', result)
    #         return result
    #     else:
    #         return result

