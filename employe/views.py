from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeSerializer
from .models import EmployeRegister
# Create your views here.

class EmployeViewSet(viewsets.ModelViewSet):
    queryset=EmployeRegister.objects.all().order_by('-id')
    serializer_class=EmployeSerializer