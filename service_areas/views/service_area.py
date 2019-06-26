from rest_framework import viewsets
from django.contrib.gis.geos import Point

from service_areas.permissions.staff_or_current import IsStaffOrCurrentUser
from service_areas.models import ServiceArea
from service_areas.serializers.service_area import ServiceAreaSerializer
from service_areas.serializers.create_service_area import (
    CreateServiceAreaSerializer
)


class ServiceAreaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsStaffOrCurrentUser,)
    serializer_class = ServiceAreaSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateServiceAreaSerializer
        return ServiceAreaSerializer

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user.provider)

    def get_queryset(self):
        queryset = ServiceArea.objects.all()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)

        if lat and lng:
            try:
                lat = float(lat)
                lng = float(lng)
            except ValueError:
                return queryset
            point = Point(x=lng, y=lat)
            queryset = queryset.filter(poly__intersects=point)
        return queryset
