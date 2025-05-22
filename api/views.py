from rest_framework import viewsets
from .models import EnergyReading
from .serializers import EnergyReadingSerializer

class EnergyReadingViewSet(viewsets.ModelViewSet):
    queryset = EnergyReading.objects.all()
    serializer_class = EnergyReadingSerializer
