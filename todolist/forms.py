from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Board


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name')


class NewTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(NewTask, self).__init__(*args, **kwargs)
        self.fields['List Name'] = forms.ModelChoiceField(queryset=Board.objects.filter(username=user))
