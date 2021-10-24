from django.urls import path
from django.contrib import admin

from rest_framework import routers

from registration.views import RegistrationView, VehicleViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', RegistrationView.as_view()),
]

#drf
router = routers.DefaultRouter()
router.register('vehicles', VehicleViewSet, basename='vehicle-list')
urlpatterns += router.urls

