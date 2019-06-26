import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_provider_get(service_area):
    client = APIClient()
    client.force_authenticate(user=service_area.provider.user)
    response = client.get(reverse(
        'service_areas-detail',
        args=(service_area.pk,)
    ))
    assert response.status_code == 200
    assert response.data['properties']['name'] == service_area.name


@pytest.mark.django_db
def test_login_required(service_area):
    client = APIClient()
    response = client.get(reverse('service_areas-detail', args=(service_area.pk,)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_available_for_admin(logged_in_admin_client, service_area):
    response = logged_in_admin_client.get(reverse(
        'service_areas-detail',
        args=(service_area.pk,)
    ))
    assert response.status_code == 200


@pytest.mark.django_db
def test_not_available_for_other_provider(logged_in_client, service_area):
    response = logged_in_client.get(reverse(
        'service_areas-detail',
        args=(service_area.pk,)
    ))
    assert response.status_code == 403
