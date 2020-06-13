from rest_framework import serializers

from trip.models import Trip
from users.serializers import UserSerializer
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    spenders = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Expense
        fields = '__all__'

class TripExpenseSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(many=True)

    class Meta:
        model = Trip
        fields = ('expense',)
