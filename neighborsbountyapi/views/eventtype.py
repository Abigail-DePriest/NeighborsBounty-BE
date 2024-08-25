from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import EventType

class EventTypeView(ViewSet):
    
    def retrieve (self, request, pk):
            eventtype = EventType.objects.get(pk=pk)
            serializer = EventTypeSerializer(eventtype)
            return Response(serializer.data, status=status.HTTP_200_OK)
          
    def list(self, request):
        eventtypes = EventType.objects.all()
        serializer = EventTypeSerializer(eventtypes, many=True)
        return Response(serializer.data)
          
          
class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'eventTypeName')
