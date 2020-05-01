from rest_framework import serializers
from .models import Category, Event
from django.contrib.auth.models import User

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()



class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Event
        fields = ("id", "name", "description", "url", "category", "category_id")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'