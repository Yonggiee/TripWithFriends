from django.conf import settings
from django.db import models
from enum import Enum
from trip.models import Trip

# Location(google map?)

# Create your models here.
class ExpenseType(Enum):
    FOOD = "Food"
    LEISURE = "Leisure"
    SOUVENIR = "Souvenir"

class Expense(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.DateField(auto_now_add=False)
    is_shared = models.BooleanField()
    money_value = models.DecimalField(max_digits=9, decimal_places=2)
    expense_type = models.CharField(max_length=8,
                                    choices=[(typ.name, typ.value)
                                             for typ in ExpenseType])
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='expense')
    spenders = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                    related_name='expense')

    def __str__(self):
        return self.name
    
