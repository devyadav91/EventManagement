from rest_framework import serializers
from .models import calender , events


class calenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = calender
        fields = ['id','user']

class eventsSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=calender.objects.all(),many=True)
    
    class Meta:
        model = events
        fields =['id','users','message','event_start','event_end']
        