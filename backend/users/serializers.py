from rest_framework import serializers
from django.conf import settings
from django.db import models
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    exposed_name = serializers.CharField(max_length=20)
    password_confirm = serializers.CharField(max_length=20)

    def validate(self, data):
        """
        Check password and password_confirm are the same
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("password and password_confirm are not the same")
        return data

    class Meta:
        model = CustomUser
        fields = (
            "email", 
            "password", 
            "password_confirm", 
            "exposed_name"
        )
