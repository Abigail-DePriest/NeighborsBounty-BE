from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Role


class RoleView(ViewSet):

    def retrieve(self, request, pk):
        role = Role.objects.get(pk=pk)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def list(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        #eventtype_id= EventType.objects.get(pk=eventtype_id)
        
        role = Role.objects.create(
            roleName=request.data['roleName']
        )
        
        serializer = RoleSerializer(role)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
      
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'roleName')
