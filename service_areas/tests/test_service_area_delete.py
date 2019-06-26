import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient

from service_areas.models import ServiceArea


@pytest.mark.django_db
def test_service_area_delete(service_area):
    pk = service_area.pk
    client = APIClient()
    client.force_authenticate(user=service_area.provider.user)
    response = client.delete(reverse(
        'service_areas-detail',
        args=(pk,)
    ))
    assert response.status_code == 204
    assert not ServiceArea.objects.filter(pk=pk).exists()


@pytest.mark.django_db
def test_login_required(service_area):
    client = APIClient()
    response = client.delete(
        reverse('service_areas-detail', args=(service_area.pk,))
    )
    assert response.status_code == 401


@pytest.mark.django_db
def test_available_for_admin(logged_in_admin_client, service_area):
    response = logged_in_admin_client.delete(reverse(
        'service_areas-detail',
        args=(service_area.pk,)
    ))
    assert response.status_code == 204


@pytest.mark.django_db
def test_not_available_for_other_provider(logged_in_client, provider, service_area):
    response = logged_in_client.delete(reverse(
        'service_areas-detail',
        args=(service_area.pk,)
    ))
    assert response.status_code == 403
