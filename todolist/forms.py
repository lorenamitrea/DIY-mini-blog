from django import forms
from django.core.exceptions import ValidationError
from .models import Task


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name')


class NewTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'board')
