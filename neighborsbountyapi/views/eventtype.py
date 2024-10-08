from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import EventType

class EventTypeView(ViewSet):
    
    def retrieve (self, request, pk):
        try:
            eventtype = EventType.objects.get(pk=pk)
        except EventType.DoesNotExist:
            return Response({"detail": "EventType not found"}, status=status.HTTP_404_NOT_FOUND)
           
            
        serializer = EventTypeSerializer(eventtype)
        return Response(serializer.data, status=status.HTTP_200_OK)
           
    def list(self, request):
        eventtypes = EventType.objects.all()
        serializer = EventTypeSerializer(eventtypes, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        #eventtype_id= EventType.objects.get(pk=eventtype_id)
        
        eventtype = EventType.objects.create(
            eventTypeName=request.data['eventTypeName']
        )
        
        serializer = EventTypeSerializer(eventtype)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        
        eventtype = EventType.objects.get(pk=pk)
        eventtype.eventTypeName = request.data['eventTypeName']
        
        eventtype.save()

        serializer = EventTypeSerializer(eventtype)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def destroy(self, request, pk):
        eventtype = EventType.objects.get(pk=pk)
        eventtype.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
          
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'eventTypeName')
        depth= 2
