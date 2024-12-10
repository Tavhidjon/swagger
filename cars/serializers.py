from rest_framework import serializers
from .models import Car, Firm

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = ['id', 'name', 'country', 'founded_year', 'description']

class CarSerializer(serializers.ModelSerializer):
    firm_name = serializers.CharField(source='firm.name', read_only=True)
    
    class Meta:
        model = Car
        fields = ['id', 'firm', 'firm_name', 'model', 'year', 'price', 
                 'description', 'image', 'created_at', 'updated_at']
