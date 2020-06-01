from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TripList

urlpatterns = [
    url(r'^trips/$', TripList.as_view(), name='trip-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
