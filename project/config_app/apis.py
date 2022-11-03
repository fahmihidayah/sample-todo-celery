from rest_framework import generics, views
from rest_framework.response import Response
from . import models
from . import serializers

class ConfigListCreateAPIView(generics.ListAPIView):
    serializer_class = serializers.ConfigurationSerializer
    authentication_classes = []
    queryset = models.Configuration.objects.all()


# class ConfigListView(views.APIView):

#     def get(self, request):
#         return Response(data={
#             'version' : "1.0"
#         })