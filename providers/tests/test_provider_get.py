import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_provider_get(provider):
    client = APIClient()
    client.force_authenticate(user=provider.user)
    response = client.get(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 200

    expected_result = {
        "user": {"email": provider.user.email},
        "name": provider.name,
        "phone_number": provider.phone_number,
        "language": provider.language,
        "currency": provider.currency
    }
    assert response.data == expected_result


@pytest.mark.django_db
def test_login_required(provider):
    client = APIClient()
    response = client.get(reverse('providers-detail', args=(provider.pk,)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_available_for_admin(logged_in_admin_client, provider):
    response = logged_in_admin_client.get(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 200


@pytest.mark.django_db
def test_not_available_for_other_provider(logged_in_client, provider):
    response = logged_in_client.get(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 403
