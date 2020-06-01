from rest_framework import serializers
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return value.username

    class Meta:
        model = settings.AUTH_USER_MODEL

