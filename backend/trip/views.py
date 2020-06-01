from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .models import Trip
from .serializers import TripSerializer

# Create your views here.

class TripList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Trip.objects.all().order_by('-trip_start')
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
