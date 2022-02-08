from .models import *
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        firlds = '__all__'
