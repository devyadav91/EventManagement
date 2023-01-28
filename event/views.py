from django.shortcuts import render
from .models import calender,events
from .serializer import eventsSerializer, calenderSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework import serializers


class EventFilter(filters.FilterSet):
    event_start = filters.DateTimeFromToRangeFilter(field_name="event_start", lookup_expr='range') 
    class Meta:
        model = events
        fields = ['event_start']



class eventapiview(ModelViewSet):
    queryset = events.objects.all()
    serializer_class = eventsSerializer    
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = EventFilter
    
    # to test that event do not over lap
    def create(self, request, *args, **kwargs):
        event_start = request.data['event_start']
        event_end = request.data['event_end']

        if event_start > event_end:
            raise serializers.ValidationError("End time can not before the start time.")

        event_start_overlap =events.objects.filter(event_start__gte=event_start,event_start__lte=event_end).exists()
        event_end_overlap = events.objects.filter(event_end__gte = event_start,event_end__lte=event_end).exists()
        enveloping_all = events.objects.filter(event_start__lte=event_start,event_end__gte=event_end).exists()

        if event_start_overlap or event_end_overlap or enveloping_all:
            raise serializers.ValidationError("Event is Overlapping !!")
        return super().create(request, *args, **kwargs)

    
class calenderapiview(ModelViewSet):
    queryset = calender.objects.all()
    serializer_class= calenderSerializer

