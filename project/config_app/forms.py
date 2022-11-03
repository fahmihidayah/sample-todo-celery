from django import forms

from . import models

class ConfigurationForm(forms.ModelForm):

    class Meta:
        model = models.Configuration
        fields = ['key', 'value']