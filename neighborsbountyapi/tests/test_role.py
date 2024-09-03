from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Role
from neighborsbountyapi.views.role import RoleSerializer

class RoleTests(APITestCase):
    # Add any fixtures you want to run to build the test database
    fixtures = ['roles']  # Ensure this matches the name of your fixture file

    def setUp(self):
        if not Role.objects.exists():
             self.role = Role.objects.create(roleName="Chef")
        else:
             self.role = Role.objects.first()

    def test_create_role(self):
        """Create Role test"""
        url = "/roles"
        new_role = {
            "roleName": "Admin"
        }

        response = self.client.post(url, new_role, format='json')

        # Get the last Role added to the database, it should be the one just created
        created_role = Role.objects.last()

        # Serialize the created Role
        expected = RoleSerializer(created_role).data

        # Test that the response data matches the expected output
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected)

    def test_get_role(self):
        """Get Role test"""
        url = f"/roles/{self.role.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Role object
        expected = RoleSerializer(self.role).data

        # Assert that the response data matches the expected output
        self.assertEqual(response.data, expected)

    def test_list_roles(self):
        """List Roles test"""
        url = "/roles"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Get all Roles from the database and serialize them
        all_roles = Role.objects.all()
        expected = RoleSerializer(all_roles, many=True).data

        # Assert that the response data matches the expected output
        self.assertEqual(response.data, expected)

    def test_update_role(self):
        """Update Role test"""
        url = f"/roles/{self.role.id}"
        updated_role = {
            "roleName": "Updated Role"
        }

        response = self.client.put(url, updated_role, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the Role object to reflect any changes in the database
        self.role.refresh_from_db()

        # Assert that the updated value matches
        self.assertEqual(updated_role['roleName'], self.role.roleName)

def test_delete_role(self):
    """Delete Role test"""
    url = f"/roles/{self.role.id}"

    # Ensure the role exists before attempting to delete
    role_exists_before = Role.objects.filter(id=self.role.id).exists()
    self.assertTrue(role_exists_before, "Role should exist before deletion")

    # Perform the delete operation
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Debug print to confirm role is deleted
    role_exists_after = Role.objects.filter(id=self.role.id).exists()
    print(f"Role exists after delete: {role_exists_after}")

    # Verify that the Role has been deleted
    self.assertFalse(role_exists_after, "Role should be deleted from the database")

    # Attempt to retrieve the deleted Role
    response = self.client.get(url)
    print(f"Retrieve response status code: {response.status_code}")
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
