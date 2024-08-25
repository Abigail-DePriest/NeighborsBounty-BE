from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Event, EventType

class EventView(ViewSet):
    
    def retrieve (self, request, pk):
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        
        eventType_id = request.data['eventType']
        eventType = EventType.objects.get(pk=eventType_id)
        
        event = Event.objects.create(
            eventDate=request.data['eventDate'],
            location=request.data['location'],
            eventTime=request.data['eventTime'],
            eventType_id=eventType_id
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
          
          
class EventSerializer(serializers.ModelSerializer):
    eventType = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())
    class Meta:
        model = Event
        fields = ('id', 'eventDate', 'eventType', 'location', 'eventTime')
