from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime
from neighborsbountyapi.models import Event, EventType
from neighborsbountyapi.views.event import EventSerializer, EventTypeSerializer

class EventTests(APITestCase):
    # Load fixtures to set up initial data
    fixtures = ['events', 'eventtypes']

    def setUp(self):
        # Set up any initial data needed for the tests
        ##self.event = Event.objects.first()  # Fetch an existing event for testing
        self.eventType = EventType.objects.create(eventTypeName="Gleaning")
        # Create an initial Event if needed
        self.event = Event.objects.create(
            eventDate="2024-12-01",
            eventType=self.eventType,
            location="Initial Location",
            eventTime="12:00"
        )
        self.url = '/events' 

    def test_create_event(self):
        """Create Event Test"""
      
        data = {
            "eventDate": "2024-12-12",
            "eventType": self.eventType.id, 
            "location": "New Location",
            "eventTime": "18:00"
        }
        
        
        print(f"Posting to URL: '/events")
        print(f"Data being sent: {data}")
        response = self.client.post(self.url, data, format='json')
        print(f"Create Event Response: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the newly created event
        new_event = Event.objects.last()
        expected = EventSerializer(new_event).data
        self.assertEqual(expected, response.data)

    def test_get_event(self):
        """Retrieve Event Test"""
        response = self.client.get(f'/events/{self.event.id}')
        print(f"Retrieve Event Response: {response.content}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected = EventSerializer(self.event).data
        self.assertEqual(expected, response.data)


    def test_list_events(self):
        """List Events Test"""
        response = self.client.get(self.url)
        
        all_events = Event.objects.all()
        expected = EventSerializer(all_events, many=True).data
        
        print(f"Expected Data: {expected}")
        print(f"Response Data: {response.data}")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_update_event(self):
        """Update Event Test"""
        updated_data = {
            "eventDate": "2024-12-13",
            "eventType": self.eventType.id,
            "location": "Updated Location",
            "eventTime": "20:00"
        }
        response = self.client.put(f"/events/{self.event.id}", updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event.refresh_from_db()
        
        updated_event_time_str = updated_data['eventTime']
        updated_event_time = datetime.strptime(updated_event_time_str, '%H:%M').time()
        
        # Compare the eventDate
        self.assertEqual(self.event.eventDate.strftime('%Y-%m-%d'), updated_data['eventDate'])
        
        # Compare the location
        self.assertEqual(self.event.location, updated_data['location'])
        
        # Compare the eventTime
        self.assertEqual(self.event.eventTime, updated_event_time)

    def test_delete_event(self):
        """Delete Event Test"""
        url = f'/events/{self.event.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
