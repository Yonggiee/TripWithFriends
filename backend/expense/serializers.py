from rest_framework import serializers

from trip.models import Trip
from profiles.serializers import ProfileSerializer
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    spenders = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Expense
        fields = '__all__'

class TripExpenseSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(many=True)

    class Meta:
        model = Trip
        fields = ('expense',)
