from django.views.generic import ListView, DetailView
from .models import MobileDevice

class DeviceListView(ListView):
    model = MobileDevice
    template_name = 'devices/device_list.html'
    context_object_name = 'devices'

class DeviceDetailView(DetailView):
    model = MobileDevice
    template_name = 'devices/device_detail.html'
    context_object_name = 'devices'
