from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Inventory

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
        try:
        
            inventory = Inventory.objects.create(
                weekStartDate=request.data['weekStartDate'],
                weekEndDate=request.data['weekEndDate'],
                pickupLocation=request.data['pickupLocation'],
                items=request.data['items']
            )
            serializer = InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
            inventory.weekStartDate = request.data['weekStartDate']
            inventory.weekEndDate = request.data['weekEndDate']
            inventory.pickupLocation = request.data['pickupLocation']
            inventory.items = request.data['items']
        
            inventory.save()
            serializer=InventorySerializer(inventory)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        inventory = Inventory.objects.get(pk=pk)
        inventory.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
##class InventorySerializer(serializers.ModelSerializer):
    ##class Meta:
      ##  model = Event
       ## fields = '__all__'  # Or specify the fields you need

class InventorySerializer(serializers.ModelSerializer):
 
  class Meta:
        model = Inventory
        fields = ('id', 'weekStartDate', 'weekEndDate', 'pickupLocation', 'items')
        depth = 3
