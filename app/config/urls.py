from django.urls import path, include
from django.contrib import admin

from .yasg import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
]
urlpatterns += swagger_urlpatterns
