from django import forms
from .models import Friend


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))


class NewTask(forms.Form):
    task_name = forms.CharField(max_length=1000, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))


class BoardShare(forms.Form):

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user')
        super(BoardShare, self).__init__(*args, **kwargs)
        users_friends = Friend.objects.filter(user_id=self.current_user)
        friends = [(entry, entry.friend.username) for entry in users_friends]
        self.fields['friend_choice'] = forms.ChoiceField(choices=friends, label='Share with')
