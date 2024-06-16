from django.contrib.auth.models import User
from django.db import models

from ..wow_guild_manager import settings


def get_class_choices():
    return settings.CLASS_CHOICES


class UserProfile(models.Model):
    """
    UserProfile class for extending standard Django user model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user', related_name='profile')
    email = models.CharField(max_length=100, verbose_name='email')
    nickname = models.CharField(max_length=20, verbose_name='nickname', unique=True)
    char_class = models.CharField(max_length=20, choices=get_class_choices())
