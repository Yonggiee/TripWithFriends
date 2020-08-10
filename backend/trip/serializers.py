from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from profiles.serializers import ProfileSerializer
from .models import Trip

class TripSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Trip
        fields = ('id', 'name', 'country', 'trip_start', 'trip_end', 'tags')

class TripDetailedSerializer(TaggitSerializer, serializers.ModelSerializer):
    members = ProfileSerializer(read_only=True, many=True)
    tags = TagListSerializerField()

    class Meta:
        model = Trip
        fields = ('id', 'name', 'desc', 
                  'country', 'members',
                  'trip_start', 'trip_end', 'tags')
