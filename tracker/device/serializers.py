from rest_framework import serializers
from .models import Device, DeviceLog

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['serial_number','name','description','condition']

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'