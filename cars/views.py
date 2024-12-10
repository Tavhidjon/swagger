from django.shortcuts import render
from rest_framework import viewsets
from .models import Car, Firm
from .serializers import CarSerializer, FirmSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.

class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'country']
    ordering_fields = ['name', 'founded_year']

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['model', 'firm__name']
    ordering_fields = ['year', 'price', 'created_at']
