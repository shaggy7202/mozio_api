import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_retrieve_all_records(logged_in_admin_client, service_area):
    response = logged_in_admin_client.get(reverse('service_areas-list'))
    assert response.status_code == 200


def test_login_required():
    client = APIClient()
    response = client.get(reverse('providers-list'))
    assert response.status_code == 401


@pytest.mark.django_db
def test_access_admin_only(logged_in_client):
    response = logged_in_client.get(reverse('providers-list'))
    assert response.status_code == 403
