from django.contrib import admin

from . import models


@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass
