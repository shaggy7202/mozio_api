from rest_framework_gis.serializers import GeoFeatureModelSerializer
from service_areas.models import ServiceArea
from providers.serializers.provider import ProviderSerializer


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """ A class to serialize service areas as GeoJSON compatible data """
    provider = ProviderSerializer()

    class Meta:
        model = ServiceArea
        geo_field = "poly"
        fields = ('name', 'price', 'provider')
