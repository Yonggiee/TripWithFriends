from rest_framework import serializers
from django.conf import settings
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.name

    class Meta:
        model = Profile
