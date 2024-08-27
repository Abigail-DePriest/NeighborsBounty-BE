from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import Member


class MemberView(ViewSet):

    def retrieve(self, request, pk):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def list(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
    
    def create(self, request):
       
        
        member = Member.objects.create(
            name=request.data['name']
        )
        
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
          
    def update(self, request, pk):
     
        member = Member.objects.get(pk=pk)
        member.uid = request.data["uid"]
        member.name= request.data["name"]
    
        member.save()
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        member = Member.objects.get(pk=pk)
        member.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    
      
      
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'uid', 'name')
