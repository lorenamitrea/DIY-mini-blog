from django import forms
from django.shortcuts import get_object_or_404

from .models import Friend, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


class NewBoard(forms.Form):
    board_name = forms.CharField(max_length=500, label='List Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))


class NewTask(forms.Form):
    task_name = forms.CharField(max_length=1000, label='',
                                widget=forms.TextInput(attrs={'class': 'form-control mr-sm-2'}))


class BoardShare(forms.Form):

    def __init__(self, *args, **kwargs):
        self.current_user = kwargs.pop('current_user')
        super().__init__(*args, **kwargs)
        users_friends = Friend.objects.filter(user_id=self.current_user)
        friends = [(entry.friend.id, entry.friend.username) for entry in users_friends]
        self.fields['friend_choice'] = forms.ChoiceField(choices=friends, label='Share with')


class UserCreationFormExtended(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save()
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NewImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mr-sm-2'}),
        }


class MessageForm(forms.Form):
    message = forms.CharField(max_length=2000, label='Write here your suggestion',
                              widget=forms.Textarea(attrs={'class': 'form-control mr-sm-2'}))

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super().__init__(*args, **kwargs)
        user_obj = get_object_or_404(User, pk=current_user)
        self.current_user = user_obj.username

    def save(self):
        send_mail(
            f'Suggestion from {self.current_user}',
            self.cleaned_data['message'],
            'todolistappdj@gmail.com',
            ['todolistappdj@gmail.com'],
            fail_silently=False,
        )
