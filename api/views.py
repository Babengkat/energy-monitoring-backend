from django.shortcuts import render

from rest_framework import viewsets
from .models import EnergyReading
from .serializers import EnergyReadingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class EnergyReadingViewSet(viewsets.ModelViewSet):
    queryset = EnergyReading.objects.all().order_by('-timestamp')
    serializer_class = EnergyReadingSerializer
    permission_classes = [AllowAny] 

