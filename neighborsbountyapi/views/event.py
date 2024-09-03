from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Event, EventType

class EventView(ViewSet):
    
    def retrieve(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
    def create(self, request):
        
        eventType_id = request.data['eventType']
        try:
             eventType = EventType.objects.get(pk=eventType_id)
        except:
            return Response({'error': 'EventType not found'}, status=status.HTTP_400_BAD_REQUEST)
            
        event = Event.objects.create(
            eventDate=request.data['eventDate'],
            location=request.data['location'],
            eventTime=request.data['eventTime'],
            eventType=eventType
        )
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):

        eventType_id = request.data['eventType']
        eventType = EventType.objects.get(pk=eventType_id)
        event = Event.objects.get(pk=pk)
        event.eventDate = request.data['eventDate']
        event.location = request.data['location']
        event.eventTime = request.data['eventTime']
        event.eventType = eventType
        event.save()

        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
          
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'eventTypeName')  
        depth = 2    
class EventSerializer(serializers.ModelSerializer):
    ##eventType = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())
    eventTime = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Event
        fields = ('id', 'eventDate', 'eventType', 'location', 'eventTime')
        depth = 2
        
   
