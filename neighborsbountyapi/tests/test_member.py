from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Member
from neighborsbountyapi.views.user import MemberSerializer

class MemberTests(APITestCase):
    
    fixtures = ['members']

    def setUp(self):
        if not Member.objects.exists():
             self.member = Member.objects.create(name="Abby")
        else:
             self.member = Member.objects.first()

    def test_create_member(self):
        """Create Member test"""
        url = "/members"
        new_member = {
            "uid": "2",
            "name": "John Doe"
            
        }

        response = self.client.post(url, new_member, format='json')
        
        created_member = Member.objects.last()

       
        expected = MemberSerializer(created_member)

       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected.data, response.data)

    def test_get_member(self):
        """Get Member test"""
        url = f"/members/{self.member.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        expected = MemberSerializer(self.member)

       
        self.assertEqual(expected.data, response.data)

    def test_list_members(self):
        """List Members test"""
        url = "/members"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        all_members = Member.objects.all()
        expected = MemberSerializer(all_members, many=True)

        
        self.assertEqual(expected.data, response.data)

    def test_update_member(self):
        """Update Member test"""
        url = f"/members/{self.member.id}"
        updated_member = {
            "uid": "3",
            "name": "Updated Name"
        }

        response = self.client.put(url, updated_member, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        self.member.refresh_from_db()

        
        self.assertEqual(updated_member['uid'], self.member.uid)
        self.assertEqual(updated_member['name'], self.member.name)

    def test_delete_member(self):
        """Delete Member test"""
        url = f"/members/{self.member.id}"

        
        member_exists_before = Member.objects.filter(id=self.member.id).exists()
        self.assertTrue(member_exists_before, "Member should exist before deletion")

       
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
        member_exists_after = Member.objects.filter(id=self.member.id).exists()
        self.assertFalse(member_exists_after, "Member should be deleted from the database")

        
        response = self.client.get(url)
        print(f"Retrieve deleted member response status: {response.status_code}")
        print(f"Retrieve deleted member response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
