from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .models import Expense
from .serializers import ExpenseSerializer

# Create your views here.

class ExpenseList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
