from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Member
from neighborsbountyapi.views.member import MemberSerializer

class MemberTests(APITestCase):
    # Load fixtures to populate the database
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

        # Get the last member added to the database, which should be the one just created
        created_member = Member.objects.last()

        # Serialize the created member
        expected = MemberSerializer(created_member)

        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(expected.data, response.data)

    def test_get_member(self):
        """Get Member test"""
        url = f"/members/{self.member.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the member object
        expected = MemberSerializer(self.member)

        # Verify the response
        self.assertEqual(expected.data, response.data)

    def test_list_members(self):
        """List Members test"""
        url = "/members"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get all members from the database and serialize them
        all_members = Member.objects.all()
        expected = MemberSerializer(all_members, many=True)

        # Verify the response
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

        # Refresh the member object to reflect any changes in the database
        self.member.refresh_from_db()

        # Verify the updated values
        self.assertEqual(updated_member['uid'], self.member.uid)
        self.assertEqual(updated_member['name'], self.member.name)

    def test_delete_member(self):
        """Delete Member test"""
        url = f"/members/{self.member.id}"

        # Ensure the member exists before attempting to delete
        member_exists_before = Member.objects.filter(id=self.member.id).exists()
        self.assertTrue(member_exists_before, "Member should exist before deletion")

        # Perform the delete operation
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Confirm the member is deleted
        member_exists_after = Member.objects.filter(id=self.member.id).exists()
        self.assertFalse(member_exists_after, "Member should be deleted from the database")

        # Attempt to retrieve the deleted Member
        response = self.client.get(url)
        print(f"Retrieve deleted member response status: {response.status_code}")
        print(f"Retrieve deleted member response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
