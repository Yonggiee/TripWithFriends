from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from trip.models import Trip
from .models import Expense
from .serializers import ExpenseSerializer, TripExpenseSerializer

# Create your views here.

class ExpenseList(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripExpenseSerializer
    pagination_class = PageNumberPagination

    def retrieve(self, request, *args, **kwargs):
        expenses = ExpenseSerializer(self.get_object().expense, many=True)
        expenses_json = expenses.data
        return Response(expenses_json)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
