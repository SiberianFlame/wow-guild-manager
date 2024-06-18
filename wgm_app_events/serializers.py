from rest_framework import serializers

from wgm_app_events.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ['id', 'owner', 'title', 'text', 'created_at', 'date']

