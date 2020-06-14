from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response

from profiles.models import Profile
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.


class UserViewSet(viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            email = serializer.data['email']
            password = serializer.data['password']
            new_user = CustomUser.objects.create(email=email, password=password)
            exposed_name = serializer.data['exposed_name']
            new_profile = Profile.objects.create(user=new_user, exposed_name=exposed_name)
            return Response(serializer.data) ## changed to remove password/created msg
        else:
            return Response(serializer.errors)
