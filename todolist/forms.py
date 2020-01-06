from django import forms


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))


class NewTask(forms.Form):
    task_name = forms.CharField(max_length=1000, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))
