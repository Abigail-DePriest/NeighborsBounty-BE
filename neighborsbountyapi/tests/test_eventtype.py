from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import EventType
from neighborsbountyapi.views.eventtype import EventTypeSerializer

class EventTypeTests(APITestCase):
    # Add any fixtures you want to run to build the test database
    fixtures = ['eventtypes']  # Assuming the fixture file is named eventtypes.json

    def setUp(self):
        # Grab the first EventType object from the database
        self.event_type = EventType.objects.create(eventTypeName="Test EventType")

    def test_create_event_type(self):
        """Create EventType test"""
        url = "/eventtypes"
        new_event_type = {
            "eventTypeName": "Workshop"
        }

        response = self.client.post(url, new_event_type, format='json')

        # Get the last EventType added to the database, it should be the one just created
        created_event_type = EventType.objects.last()

        # Serialize the created EventType
        expected = EventTypeSerializer(created_event_type)

        # Test that the response data matches the expected output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected.data, response.data)

    def test_get_event_type(self):
        """Get EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the EventType object
        expected = EventTypeSerializer(self.event_type)

        # Assert that the response data matches the expected output
        self.assertEqual(expected.data, response.data)

    def test_list_event_types(self):
        """List EventTypes test"""
        url = "/eventtypes"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get all EventTypes from the database and serialize them
        all_event_types = EventType.objects.all()
        expected = EventTypeSerializer(all_event_types, many=True)

        # Assert that the response data matches the expected output
        self.assertEqual(expected.data, response.data)

    def test_update_event_type(self):
        """Update EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        updated_event_type = {
            "eventTypeName": "Updated Name"
        }

        response = self.client.put(url, updated_event_type, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the EventType object to reflect any changes in the database
        self.event_type.refresh_from_db()

        # Assert that the updated value matches
        self.assertEqual(updated_event_type['eventTypeName'], self.event_type.eventTypeName)

    def test_delete_event_type(self):
        """Delete EventType test"""
        url = f"/eventtypes/{self.event_type.id}"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Attempt to retrieve the deleted EventType
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
