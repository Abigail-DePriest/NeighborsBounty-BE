from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from neighborsbountyapi.models import User


class UserView(ViewSet):

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("Member not found.")
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def create(self, request):
       
        
        user = User.objects.create(
            
            uid=request.data['uid'],
            name=request.data['name']
            
        )
        
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
          
    def update(self, request, pk):
     
        user = User.objects.get(pk=pk)
        user.uid = request.data["uid"]
        user.name= request.data["name"]
    
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    
      
      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'name')
        depth = 2
