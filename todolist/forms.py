from django import forms
from django.core.exceptions import ValidationError
from .models import Task, Board
from django.utils.translation import ugettext_lazy as _


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name')


class NewTask(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name',)
        #labels = {'name': _('Task Name')}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', '')
        super(NewTask, self).__init__(*args, **kwargs)
        self.fields['board'] = forms.ModelChoiceField(queryset=Board.objects.filter(username=user))
        #self.labels['board'] = _('List Name')
