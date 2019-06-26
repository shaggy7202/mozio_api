from rest_framework import serializers
from providers.models import Provider
from providers.serializers.user import UserSerializer


class ProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Provider
        fields = (
            'user',
            'name',
            'phone_number',
            'language',
            'currency'
        )
