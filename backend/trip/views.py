from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expense.models import Expense
from expense.serializers import ExpenseSerializer, TripExpenseSerializer
from profiles.models import Profile
from .models import Trip
from .serializers import TripSerializer, TripDetailedSerializer

# Create your views here.

class TripViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    serializer_class = TripSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)
        return Trip.objects.filter(members__in=[profile]).order_by('-trip_start')

    def get_serializer_class(self):
        if self.action == 'list':
            return TripSerializer
        if self.action == 'retrieve':
            return TripDetailedSerializer
        if self.action == 'create':
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
    
    @action(methods=['post'], detail=True,
            url_path='expense', url_name='post-expense')
    def post_expense(self, request, pk=None):
        serializer = ExpenseSerializer(data=request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
