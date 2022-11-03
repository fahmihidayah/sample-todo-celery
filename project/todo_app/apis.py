from rest_framework import generics
from . import models
from . import serializers


class TodoListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.TodoSerializer
    authentication_classes = []
    queryset = models.Todo.objects.all()

    def list(self, request, *args, **kwargs):
        return super(TodoListCreateAPIView, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(TodoListCreateAPIView, self).create(request, *args, **kwargs)


class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TodoSerializer
    authentication_classes = []
    queryset = models.Todo.objects.all()

    def get_object(self):
        return super(TodoRetrieveUpdateDestroyAPIView, self).get_object()

    def retrieve(self, request, *args, **kwargs):
        return super(TodoRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TodoRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(TodoRetrieveUpdateDestroyAPIView, self).update(request, *args, **kwargs)

