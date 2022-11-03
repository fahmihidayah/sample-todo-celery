from pyexpat import model
from django.db import models

# Create your models here.


class Configuration(models.Model):

    key: models.CharField = models.CharField(max_length=100)

    value: models.CharField = models.CharField(max_length=200)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return self.key