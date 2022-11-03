from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Todo(models.Model):

    title: models.CharField = models.CharField(max_length=100)

    description: models.TextField = models.TextField(max_length=2000)

    user: models.ForeignKey = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True, editable=False)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True, editable=False)
