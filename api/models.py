from django.db import models

class EnergyReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    current = models.FloatField(help_text="Current in Amperes")
    power = models.FloatField(help_text="Power in Watts")
    energy = models.FloatField(help_text="Energy in kWh")
    building = models.CharField(max_length=100, default="Building A")

    def __str__(self):
        return f"{self.building} | {self.timestamp} | {self.energy} kWh"
