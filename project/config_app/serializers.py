from rest_framework import serializers
from . import models

class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Configuration
        fields = ['key', 'value', 'created_at', 'updated_at']