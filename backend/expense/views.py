from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from trip.models import Trip
from .models import Expense
from .serializers import ExpenseSerializer, TripExpenseSerializer

# Create your views here.

class ExpenseList(mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripExpenseSerializer

    def get(self, request, *args, **kwargs):
        expenses = ExpenseSerializer(self.get_object().expense, many=True)
        expenses_json = expenses.data
        return Response(expenses_json)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
