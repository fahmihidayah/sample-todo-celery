from . import apis
from django.urls import path

urlpatterns = [
    path('api/v1/configurations', apis.ConfigListCreateAPIView.as_view(), name='api_v1_configurations'),
]