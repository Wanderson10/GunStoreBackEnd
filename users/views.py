from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

class LoginView(generics.CreateAPIView):
    ...

class UserView(generics.ListCreateAPIView):
    
    serializer_class = UserSerializer
  
    queryset = User.objects.all()
    
    ...

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
  
    queryset = User.objects.all()
    
    lookup_url_kwarg = 'user_id'
     