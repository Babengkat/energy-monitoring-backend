from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnergyReadingViewSet


router = DefaultRouter()
router.register(r'energy-readings', EnergyReadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
