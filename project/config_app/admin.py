from django.contrib import admin
from . import models
from . import forms
# Register your models here.

@admin.register(models.Configuration)
class ConfigurationModelAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'created_at', 'updated_at']
    search_fields = ['key', 'value']
    form = forms.ConfigurationForm