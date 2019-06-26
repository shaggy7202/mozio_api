import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient
from service_areas.models import ServiceArea


@pytest.mark.django_db
def test_create_provider(provider):
    client = APIClient()
    client.force_authenticate(user=provider.user)
    data = {
        "name": "POST TEST",
        "price": "100.0",
        "poly": {
            "type": "Polygon",
            "coordinates": [
                [[24.301757809117316,50.51342652114294],
                 [25.488281246452164,49.979487755905694],
                 [23.598632809215417,48.95136646580187],
                 [22.895507809313518,49.58222603945369],
                 [23.203124996770768,49.86631672436136],
                 [24.301757809117316,50.51342652114294]]
            ]
        }
    }
    response = client.post(reverse('service_areas-list'), data, format='json')
    assert response.status_code == 201
    service_area = ServiceArea.objects.get(name=data['name'])
    assert service_area.provider.pk == provider.pk
    assert service_area.price == float(data['price'])
