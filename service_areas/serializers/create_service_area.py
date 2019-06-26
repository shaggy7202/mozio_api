from rest_framework_gis.serializers import GeoFeatureModelSerializer
from service_areas.models import ServiceArea


class CreateServiceAreaSerializer(GeoFeatureModelSerializer):
    """ A class to serialize service areas as GeoJSON compatible data """

    class Meta:
        model = ServiceArea
        geo_field = "poly"
        fields = ('name', 'price')
