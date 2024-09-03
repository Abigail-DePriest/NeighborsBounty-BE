from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Inventory, Event, EventType
from neighborsbountyapi.views.inventory import InventorySerializer

class InventoryTests(APITestCase):
    
    # Add any fixtures you want to run to build the test database
    fixtures = ['inventory', 'events', 'eventtypes']

    def setUp(self):
        eventType=EventType.objects.get(pk=1)
        self.event = Event.objects.create(
            eventDate='2024-09-10',
            eventType=eventType,
            location='Sample Location',
            eventTime='12:00'
        )
        self.inventory = Inventory.objects.create(
            foodType='Apples',
            quantity=30,
            pickupDate='2024-08-16',
            pickupLocation='Test Location',
            event=self.event
        )
            
    def test_create_inventory(self):
        """Create inventory test"""
        url = "/inventories"
        data = {
            "foodType": "carrots",
            "quantity": 15,
            "pickupDate": "2024-09-16",
            "pickupLocation": "Downtown Market",
            "event": self.event.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        new_inventory = Inventory.objects.last()
        expected = InventorySerializer(new_inventory).data
        self.assertEqual(response.data, expected)

    def test_get_inventory(self):
        """Get inventory test"""
        url = f'/inventories/{self.inventory.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected = InventorySerializer(self.inventory).data
        self.assertEqual(len(response.data), len(expected))

    def test_list_inventories(self):
        """List inventories test"""
        url = '/inventories'
        response = self.client.get(url)
        
        all_inventories = Inventory.objects.all()
        expected = InventorySerializer(all_inventories, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_update_inventory(self):
        """Update inventory test"""
        url = f'/inventories/{self.inventory.id}'
        data = {
            "foodType": "sweet potatoes",
            "quantity": 25,
            "pickupDate": "2024-10-16",
            "pickupLocation": "Westside Market",
            "event": self.event.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        updated_inventory = Inventory.objects.get(pk=self.inventory.id)
        self.assertEqual(updated_inventory.foodType, data['foodType'])
        self.assertEqual(updated_inventory.quantity, data['quantity'])

    def test_delete_inventory(self):
        # Define the URL to delete the inventory item
        url = f"/inventories/{self.inventory.id}"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Attempt to retrieve the deleted EventType
      ##  response = self.client.get(url)
       ## self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
