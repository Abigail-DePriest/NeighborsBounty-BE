from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import EventType
from neighborsbountyapi.views.eventtype import EventTypeSerializer

class EventTypeTests(APITestCase):
 
    fixtures = ['eventtypes']  

    def setUp(self):
        
        self.event_type = EventType.objects.create(eventTypeName="Test EventType")

    def test_create_event_type(self):
        """Create EventType test"""
        url = "/eventtypes"
        new_event_type = {
            "eventTypeName": "Workshop"
        }

        response = self.client.post(url, new_event_type, format='json')
       
        created_event_type = EventType.objects.last()
        
        expected = EventTypeSerializer(created_event_type)

        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected.data, response.data)

    def test_get_event_type(self):
        """Get EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        expected = EventTypeSerializer(self.event_type)
        
        self.assertEqual(expected.data, response.data)

    def test_list_event_types(self):
        """List EventTypes test"""
        url = "/eventtypes"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        all_event_types = EventType.objects.all()
        expected = EventTypeSerializer(all_event_types, many=True)

   
        self.assertEqual(expected.data, response.data)

    def test_update_event_type(self):
        """Update EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        updated_event_type = {
            "eventTypeName": "Updated Name"
        }

        response = self.client.put(url, updated_event_type, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        self.event_type.refresh_from_db()

   
        self.assertEqual(updated_event_type['eventTypeName'], self.event_type.eventTypeName)

    def test_delete_event_type(self):
        """Delete EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
