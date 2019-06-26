import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_retrieve_all_records(logged_in_admin_client, provider):
    expected_data = [{
        "user": {"email": provider.user.email},
        "name": provider.name,
        "phone_number": provider.phone_number,
        "language": provider.language,
        "currency": provider.currency
    }]
    response = logged_in_admin_client.get(reverse('providers-list'))
    assert response.data == expected_data


def test_login_required():
    client = APIClient()
    response = client.get(reverse('providers-list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_access_admin_only(logged_in_client):
    response = logged_in_client.get(reverse('providers-list'))
    assert response.status_code == 403
