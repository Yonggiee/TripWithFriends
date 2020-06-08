from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets

from .models import Trip
from .serializers import TripSerializer

# Create your views here.

class TripList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Trip.objects.all().order_by('-trip_start')
    serializer_class = TripSerializer

