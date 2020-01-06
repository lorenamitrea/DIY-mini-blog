from django import template
from ..models import Friend

register = template.Library()


@register.simple_tag
def is_friend(user, friend):
    relation = Friend.objects.filter(user=user, friend=friend)
    return False if not relation else True
