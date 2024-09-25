from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import SignUp, Member, Event, Role, EventType
from neighborsbountyapi.views.signup import SignUpSerializer

class SignUpTests(APITestCase):

   
    fixtures = ['events','eventtypes','members', 'roles', 'signups']

    def setUp(self):
        
        self.eventType=EventType.objects.get(pk=1)
        self.member = Member.objects.get(pk=1)
        self.event = Event.objects.get(pk=1)
        self.role = Role.objects.get(pk=1)
        
        
        self.signup = SignUp.objects.create(
            member=self.member,
            event=self.event,
            role=self.role
        )

    def test_create_signup(self):
        """Create signup test"""
        url = "/signups"
        data = {
            "member": self.member.id,
            "event": self.event.id,
            "role": self.role.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        new_signup = SignUp.objects.last()
        expected = SignUpSerializer(new_signup).data
        self.assertEqual(response.data, expected)

    def test_get_signup(self):
        """Get signup test"""
        url = f'/signups/{self.signup.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        expected = SignUpSerializer(self.signup).data
        self.assertEqual(response.data, expected)

    def test_list_signups(self):
        """List signups test"""
        url = '/signups'
        response = self.client.get(url)
        
        all_signups = SignUp.objects.all()
        expected = SignUpSerializer(all_signups, many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    def test_update_signup(self):
        """Update signup test"""
        url = f'/signups/{self.signup.id}'
        new_role = Role.objects.exclude(pk=self.role.id).first()
        data = {
            "member": self.member.id,
            "event": self.event.id,
            "role": new_role.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        updated_signup = SignUp.objects.get(pk=self.signup.id)
        self.assertEqual(updated_signup.role, new_role)

    def test_delete_signup(self):
        """Delete signup test"""
        url = f'/signups/{self.signup.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
