from django.shortcuts import render
from rest_framework import generics, viewsets
from myapp.serializers import EventSerializer, UserSerializer
from myapp.models import Event, User



class Eventgenerics(generics.ListCreateAPIView):
    queryset = Event
    serializer_class = EventSerializer


class Usergenerics (generics.ListCreateAPIView):
    queryset = User
    serializer_class = UserSerializer