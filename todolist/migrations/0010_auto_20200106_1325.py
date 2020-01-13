# Generated by Django 2.2.7 on 2020-01-06 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0009_auto_20200103_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='username',
        ),
        migrations.AddField(
            model_name='board',
            name='username',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
