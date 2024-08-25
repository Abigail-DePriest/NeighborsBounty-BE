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
          
          
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = ('id', 'member_id', 'event_id', 'role_id')
