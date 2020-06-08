from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseList

# Create a router and register our viewsets with it.
expense_router = DefaultRouter()
expense_router.register(r'trip', ExpenseList, basename='expenses')

