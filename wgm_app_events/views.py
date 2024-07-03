from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics

from wgm_app_events.models import EventModel
from wgm_app_events.serializers import EventSerializer


class EventsList(generics.ListCreateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
