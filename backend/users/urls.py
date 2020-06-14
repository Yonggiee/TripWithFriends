from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Create a router and register our viewsets with it.
user_router = DefaultRouter()
user_router.register(r'user', UserViewSet)
