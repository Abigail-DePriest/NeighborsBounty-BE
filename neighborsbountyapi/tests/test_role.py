from rest_framework import status
from rest_framework.test import APITestCase
from neighborsbountyapi.models import Role
from neighborsbountyapi.views.role import RoleSerializer

class RoleTests(APITestCase):
    
    fixtures = ['roles']  
    
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

        
        created_role = Role.objects.last()

      
        expected = RoleSerializer(created_role).data

        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected)

    def test_get_role(self):
        """Get Role test"""
        url = f"/roles/{self.role.id}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        expected = RoleSerializer(self.role).data

        
        self.assertEqual(response.data, expected)

    def test_list_roles(self):
        """List Roles test"""
        url = "/roles"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        all_roles = Role.objects.all()
        expected = RoleSerializer(all_roles, many=True).data

        
        self.assertEqual(response.data, expected)

    def test_update_role(self):
        """Update Role test"""
        url = f"/roles/{self.role.id}"
        updated_role = {
            "roleName": "Updated Role"
        }

        response = self.client.put(url, updated_role, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        self.role.refresh_from_db()

        
        self.assertEqual(updated_role['roleName'], self.role.roleName)

def test_delete_role(self):
    """Delete Role test"""
    url = f"/roles/{self.role.id}"

    
    role_exists_before = Role.objects.filter(id=self.role.id).exists()
    self.assertTrue(role_exists_before, "Role should exist before deletion")

    
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    role_exists_after = Role.objects.filter(id=self.role.id).exists()
    print(f"Role exists after delete: {role_exists_after}")

    
    self.assertFalse(role_exists_after, "Role should be deleted from the database")

    
    response = self.client.get(url)
    print(f"Retrieve response status code: {response.status_code}")
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
