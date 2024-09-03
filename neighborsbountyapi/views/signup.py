from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from neighborsbountyapi.models import SignUp, Member, Event, Role

class SignUpView(ViewSet):
    
    def retrieve (self, request, pk):
        try:
            signup = SignUp.objects.get(pk=pk)
            serializer = SignUpSerializer(signup)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except SignUp.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        signups = SignUp.objects.all()
        serializer = SignUpSerializer(signups, many=True)
        return Response(serializer.data)
          
    def create(self, request):
        
        event_id = request.data['event']
        role_id = request.data['role']
        member_id = request.data['member']
        
        member = Member.objects.get(pk=member_id)
        event = Event.objects.get(pk=event_id)
        role = Role.objects.get(pk=role_id)
        
        signup = SignUp.objects.create(
            member=member,
            event=event,
            role=role
            
            
        )
        serializer = SignUpSerializer(signup)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        member_id = request.data['member']
        event_id = request.data['event']
        role_id = request.data['role']
        
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
    
class EventSerializer(serializers.ModelSerializer):
   class Meta:
        model = Event
        fields = ('id', 'eventDate', 'eventType', 'location', 'eventTime')
        depth = 2
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'roleName')
        depth = 2
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'uid', 'name')
        depth = 2
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'member', 'event', 'role')
        depth = 2
