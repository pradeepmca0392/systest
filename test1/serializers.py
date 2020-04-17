from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = Status
    fields = ('id', 'Name', 'Shop_Name', 'Status', 'Date')