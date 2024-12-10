from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, FirmViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'firms', FirmViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
