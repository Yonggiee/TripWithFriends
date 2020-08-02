from rest_framework.routers import DefaultRouter
from .views import TripViewSet

# Create a router and register our viewsets with it.
trip_router = DefaultRouter()
trip_router.register(r'trips', TripViewSet, basename='Trip')
