from django.contrib.auth.models import User
from django.db import models


class EventModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=20, verbose_name='title')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation time and date')
    date = models.DateTimeField(verbose_name='date')

    def __str__(self):
        return f'{self.title} event by {self.owner} at {self.date}'

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

