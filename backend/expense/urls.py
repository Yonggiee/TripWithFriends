from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ExpenseList

urlpatterns = [
    url(r'^trip/(?P<pk>[0-9]+)/expenses/$',
        ExpenseList.as_view(), name='trip-expenses')
]

urlpatterns = format_suffix_patterns(urlpatterns)
