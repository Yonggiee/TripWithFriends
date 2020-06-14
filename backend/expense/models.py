from django.conf import settings
from django.db import models
from enum import Enum

from trip.models import Trip
from profiles.models import Profile

# Location(google map?)

# Create your models here.
class ExpenseType(Enum):
    FOOD = "Food"
    LEISURE = "Leisure"
    SOUVENIR = "Souvenir"

class Expense(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    date = models.DateField(auto_now_add=False, blank=True, null=True)
    money_value = models.DecimalField(max_digits=9, decimal_places=2)
    expense_type = models.CharField(max_length=8,
                                    choices=[(typ.name, typ.value)
                                             for typ in ExpenseType])
    trip = models.ForeignKey(Trip,
                             on_delete=models.CASCADE,
                             related_name='expense')
    spenders = models.ManyToManyField(Profile, 
                                    related_name='expense')

    def __str__(self):
        spenders = ','.join(str(spender) for spender in self.spenders.all())
        return "{}, {{{}}}".format(self.name, spenders)
    
