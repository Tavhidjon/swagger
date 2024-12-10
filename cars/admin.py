from django.contrib import admin
from .models import Car, Firm

# Register your models here.

@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'country')
    list_filter = ('country',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'firm', 'year', 'price')
    list_filter = ('firm', 'year')
    search_fields = ('model', 'firm__name')
    date_hierarchy = 'created_at'
