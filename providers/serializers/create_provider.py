from rest_framework import serializers
from providers.models import Provider
from providers.serializers.create_user import CreateUserSerializer
from django.contrib.auth.models import User


class CreateProviderSerializer(serializers.ModelSerializer):
    user = CreateUserSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['username'] = user_data['email']
        user = User.objects.create_user(**user_data)
        validated_data['user'] = user
        provider = Provider(**validated_data)
        provider.save()
        return provider

    class Meta:
        model = Provider
        fields = (
            'user',
            'name',
            'phone_number',
            'language',
            'currency'
        )
