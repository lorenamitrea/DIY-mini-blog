from django import forms
from django.core.exceptions import ValidationError


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name')


class NewTask(forms.Form):
    task_name = forms.CharField(max_length=1000, label='')


