from django.contrib import admin
from . import models
from . import forms
from . import tasks
# Register your models here.

@admin.register(models.Todo)
class TodoModelAdmin(admin.ModelAdmin):
    form = forms.TodoForm
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        super(TodoModelAdmin, self).save_model(request, obj, form, change)
        tasks.send_email.delay(obj.pk)
