from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from users.serializers import UserSerializer
from .models import Trip

class TripSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Trip
        fields = ('id', 'name', 'trip_start', 'trip_end', 'tags')

class TripDetailedSerializer(TaggitSerializer, serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)
    tags = TagListSerializerField()

    class Meta:
        model = Trip
        fields = ('id', 'name', 'desc', 'members',
                  'trip_start', 'trip_end', 'tags')
