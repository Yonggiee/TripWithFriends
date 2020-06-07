from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Trip

class TripSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Trip
        fields = ('name', 'desc', 'members', 'trip_start', 'trip_end')
