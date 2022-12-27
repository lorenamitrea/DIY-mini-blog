from django.contrib import admin
from .models import Board, Task, Friend, Image, UserImages

admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Friend)
admin.site.register(Image)
admin.site.register(UserImages)
