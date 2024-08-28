from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Event, EventType

class EventTests(APITestCase):

    def setUp(self):
        # Create some initial EventType data
        self.eventtype1 = EventType.objects.create(eventTypeName='Gleaning')
        self.eventtype2 = EventType.objects.create(eventTypeName='Cooking')

        # Create some initial Event data
        self.event1 = Event.objects.create(
            eventDate='2024-09-10',
            eventType=self.eventtype1,
            location='567 Straight to Heaven, God\'s house',
            eventTime='11:00'
        )
        self.event2 = Event.objects.create(
            eventDate='2024-10-10',
            eventType=self.eventtype2,
            location='123 cooking street, Abby\'s house',
            eventTime='15:00'
        )

        # Define URLs
        self.url = '/events/'  # Endpoint for listing and creating
        self.detail_url = f'/events/{self.event1.pk}/'  # Endpoint for detail, update, and delete

    def test_list_events(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check that there are 2 events in the response

    def test_retrieve_event(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['eventDate'], '2024-09-10')
        self.assertEqual(response.data['eventType'], self.eventtype1.pk)

    def test_create_event(self):
        data = {
            'eventDate': '2024-11-11',
            'eventType': self.eventtype1.pk,
            'location': 'West Side Encampment',
            'eventTime': '19:00'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 3)
  
