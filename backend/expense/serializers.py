from rest_framework import serializers

from user.serializers import UserSerializer
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    spenders = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Expense
        fields = '__all__'
