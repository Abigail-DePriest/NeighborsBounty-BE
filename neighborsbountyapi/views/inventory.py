from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Inventory, Event

class InventoryView(ViewSet):
    
    def retrieve (self, request, pk):
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_200_OK)
          
    def list(self, request):
        inventories = Inventory.objects.all()
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)
    
          
    def create(self, request):
        
        event_id = request.data['event']
        event = Event.objects.get(pk=event_id)
        
        inventory = Inventory.objects.create(
            foodType=request.data['foodType'],
            quantity=request.data['quantity'],
            pickupDate=request.data['pickupDate'],
            pickupLocation=request.data['pickupDate'],
            event=event
        )
        serializer = InventorySerializer(inventory)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Or specify the fields you need

class InventorySerializer(serializers.ModelSerializer):
 
  class Meta:
        model = Inventory
        fields = ('id', 'foodType', 'quantity', 'pickupDate', 'pickupLocation', 'event')
        depth = 2
