from rest_framework import serializers
from .models import EmployeRegister


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeRegister
        fields = ('id', 'full_name', 'email', 'address')