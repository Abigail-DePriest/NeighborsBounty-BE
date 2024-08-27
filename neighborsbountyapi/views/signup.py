from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import SignUp, Member, Event, Role

class SignUpView(ViewSet):
    
    def retrieve (self, request, pk):
            signup = SignUp.objects.get(pk=pk)
            serializer = SignUpSerializer(signup)
            return Response(serializer.data, status=status.HTTP_200_OK)
          
    def list(self, request):
        signups = SignUp.objects.all()
        serializer = SignUpSerializer(signups, many=True)
        return Response(serializer.data)
          
    def create(self, request):
        
        event_id = request.data['event_id']
        event_id = Event.objects.get(pk=event_id)
        member_id = request.data['member_id']
        member_id = Member.objects.get(pk=member_id)
        role_id = request.data['role_id']
        role_id = Role.objects.get(pk=role_id)
        
        signup = SignUp.objects.create(
            member_id=request.data['member_id'],
            event_id=request.data['event_id'],
            role_id=request.data['role_id'],
            member=member_id,
            event=event_id,
            role=role_id
            
            
        )
        serializer = SignUpSerializer(signup)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        member_id = request.data['member_id']
        event_id = request.data['event_id']
        role_id = request.data['role_id']
        
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        
        signup = SignUp.objects.get(pk=pk)
        signup.member= member
        signup.event = event
        signup.role = role
    
        signup.save()
        serializer = SignUpSerializer(signup)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        signup = SignUp.objects.get(pk=pk)
        signup.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'member_id', 'event_id', 'role_id')
