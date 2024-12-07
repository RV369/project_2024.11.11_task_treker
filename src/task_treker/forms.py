from django import forms
from django.contrib.auth import get_user_model

from .models import AppointedPerformer, Task, VerifiedTask

User = get_user_model()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description',)


class AppointedPerformerForm(forms.ModelForm):
    class Meta:
        model = AppointedPerformer
        fields = ('performer',)
        required_css_class = 'field'
        error_css_class = 'error'


class VerifiedTaskForm(forms.ModelForm):
    class Meta:
        model = VerifiedTask
        fields = ('reviewer',)
