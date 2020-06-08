from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from trip.models import Trip
from .models import Expense
from .serializers import ExpenseSerializer, TripExpenseSerializer

# Create your views here.

class ExpenseList(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripExpenseSerializer
    pagination_class = PageNumberPagination

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

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
