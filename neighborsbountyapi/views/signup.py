from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from neighborsbountyapi.models import SignUp, User, Event

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
        try:
            event_id = request.data['event']
            user_id = request.data['user']
            
            user = User.objects.get(pk=user_id)
            event = Event.objects.get(pk=event_id)
            signup = SignUp.objects.create(
                user=user,
                event=event,
                
                
            )
            serializer = SignUpSerializer(signup)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'detail': f'Missing key: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Event.DoesNotExist:
            return Response({'detail': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, pk):
        user_id = request.data['user']
        event_id = request.data['event']
       
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
            
        
        signup = SignUp.objects.get(pk=pk)
        signup.user= user
        signup.event = event
       
    
        signup.save()
        serializer = SignUpSerializer(signup)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=False, url_path='get_user_signups')
    def get_user_signups(self, request, pk=None):
        user = User.objects.get(pk=request.data["user"])
        
        serializer = UserSerializer(user)
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
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'uid', 'name', 'events')
        depth = 2
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'user', 'event')
        depth = 2
