from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

from expense.serializers import ExpenseSerializer, TripExpenseSerializer
from .models import Trip
from .serializers import TripSerializer, TripDetailedSerializer

# Create your views here.

class TripList(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    queryset = Trip.objects.all().order_by('-trip_start')
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return TripSerializer
        if self.action == 'retrieve':
            return TripDetailedSerializer
        return TripSerializer

    @action(methods=['get'], detail=True,
            url_path='expenses', url_name='get-expenses')
    def get_expenses(self, request, pk=None):
        queryset = self.get_object().expense.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            expenses = ExpenseSerializer(page, many=True)
            expenses_json = expenses.data
            return self.get_paginated_response(expenses_json)
        expenses = ExpenseSerializer(queryset, many=True)
        expenses_json = expenses.data
        return Response(expenses_json)
