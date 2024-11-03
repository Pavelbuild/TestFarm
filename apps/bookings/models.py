from django.db import models
from django.contrib.auth import get_user_model
from apps.devices.models import MobileDevice

User = get_user_model()

class Booking(models.Model):
    device = models.ForeignKey(MobileDevice,on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.device.name}"
