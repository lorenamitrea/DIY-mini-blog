from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=500)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
    details = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.board}'


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    friend = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='friends', null=True)

    def __str__(self):
        return f'{self.user.username} is friend with {self.friend.username}.'
