from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from service_areas.models import ServiceArea


@admin.register(ServiceArea)
class ServiceAreaAdmin(OSMGeoAdmin):
    list_display = ('name',)
