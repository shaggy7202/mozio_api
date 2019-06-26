from rest_framework import viewsets

from providers.permissions.staff_or_current import IsStaffOrCurrentUser
from providers.models import Provider
from providers.serializers.create_provider import CreateProviderSerializer
from providers.serializers.provider import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = (IsStaffOrCurrentUser,)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProviderSerializer
        return ProviderSerializer
