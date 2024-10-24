from django.db import models
from django.contrib.auth import get_user_model

# custom user model
User  = get_user_model()

class MobileDevice(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='device_photo/', blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    operating_system = models.CharField(max_length=50, null=True, blank=True)
    cpu_model = models.CharField(max_length=50, null=True, blank=True)
    ram_memory = models.IntegerField(null=True, blank=True)
    storage_memory = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking_start_time = models.DateTimeField(null=True, blank=True)
    booking_end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name