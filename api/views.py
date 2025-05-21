from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import EnergyReading
from .serializers import EnergyReadingSerializer


class EnergyReadingViewSet(viewsets.ModelViewSet):
    queryset = EnergyReading.objects.all().order_by('-timestamp')
    serializer_class = EnergyReadingSerializer