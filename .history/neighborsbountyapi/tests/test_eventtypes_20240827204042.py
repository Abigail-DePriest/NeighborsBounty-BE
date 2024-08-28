from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import EventType

class EventTypeTests(APITestCase):

    def setUp(self):
        # Set up initial data
        self.eventtype1 = EventType.objects.create(eventTypeName='Gleaning')
        self.eventtype2 = EventType.objects.create(eventTypeName='Cooking')
        self.url = '/eventtypes/'  # Endpoint for listing and creating
        self.detail_url = f'/eventtypes/{self.eventtype1.pk}/'  # Endpoint for detail, update, and delete

    def test_list_eventtypes(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure there are 2 event types in the response

    def test_retrieve_eventtype(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['eventTypeName'], 'Gleaning')

    def test_create_eventtype(self):
        data = {'eventTypeName': 'Distribution'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EventType.objects.count(), 3)
        self.assertEqual(EventType.objects.get(pk=response.data['id']).eventTypeName, 'Distribution')

    def test_update_eventtype(self):
        data = {'eventTypeName': 'Updated EventType'}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(EventType.objects.get(pk=self.eventtype1.pk).eventTypeName, 'Updated EventType')

    def test_destroy_eventtype(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EventType.objects.count(), 1)  # Only one should remain after deletion

    def test_create_eventtype_missing_field(self):
        # Test creating an event type without 'eventTypeName'
        data = {}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('eventTypeName', response.data)  # Ensure error message for missing field
