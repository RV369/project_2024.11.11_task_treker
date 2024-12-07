from django import forms

from .models import Task, VerifiedTask, AppointedPerformer
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description',)


class AppointedPerformerForm(forms.ModelForm):
    class Meta:
        model = AppointedPerformer
        fields = ('performer',)
        required_css_class = "field"
        error_css_class = "error"


class VerifiedTaskForm(forms.ModelForm):
    class Meta:
        model = VerifiedTask
        fields = ('reviewer',)


