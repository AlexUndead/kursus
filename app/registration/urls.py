from django.urls import path

from rest_framework import routers

from .views import RegistrationView, VehicleViewSet

urlpatterns = [
    path('registration/', RegistrationView.as_view()),
]

router = routers.DefaultRouter()
router.register('vehicles', VehicleViewSet, basename='vehicle-list')
urlpatterns += router.urls
