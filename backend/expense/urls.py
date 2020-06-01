from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ExpenseList

urlpatterns = [
    url(r'^expenses/$', ExpenseList.as_view(), name='expense-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
