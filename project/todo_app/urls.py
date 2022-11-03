from django.urls import path
from . import apis
from . import views

urlpatterns = [
    path('api/v1/todos',apis.TodoListCreateAPIView.as_view(), name='api_v1_todos'),
    path('api/v1/todos/<int:pk>', apis.TodoRetrieveUpdateDestroyAPIView.as_view(), name='api_v1_todos_id'),

    path('todos', views.TodoListView.as_view(), name='view_todos'),
]