from rest_framework import serializers
from .models import Event, RSVP

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['id','image', 'title', 'description', 'date_time', 'location', 'guest_limit']

class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ['id', 'event', 'user', 'status']
        read_only_fields = ['user']