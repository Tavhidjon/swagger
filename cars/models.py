from django.db import models

# Create your models here.

class Firm(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Car(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.firm.name} {self.model} ({self.year})"
