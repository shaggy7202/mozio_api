import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_provider_update(provider):
    client = APIClient()
    client.force_authenticate(user=provider.user)
    response = client.patch(reverse(
        'providers-detail',
        args=(provider.pk,)
    ), {"name": "Updated name"})
    assert response.status_code == 200
    assert response.data['name'] == "Updated name"


@pytest.mark.django_db
def test_login_required(provider):
    client = APIClient()
    response = client.patch(reverse('providers-detail', args=(provider.pk,)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_available_for_admin(logged_in_admin_client, provider):
    response = logged_in_admin_client.patch(reverse(
        'providers-detail',
        args=(provider.pk,)
    ), {"name": "Updated name"})
    assert response.status_code == 200
    assert response.data['name'] == "Updated name"


@pytest.mark.django_db
def test_not_available_for_other_provider(logged_in_client, provider):
    response = logged_in_client.patch(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 403
