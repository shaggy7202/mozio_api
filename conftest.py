import pytest
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.contrib.gis.geos import Polygon

from providers.models import Provider
from service_areas.models import ServiceArea


@pytest.fixture
def logged_in_client():
    user = User.objects.create_user(
        username='test@gmail.com',
        email='test@gmail.com',
        password='testtesttest',
        is_active=True
    )
    data = {
        'username': user.username,
        'password': 'testtesttest'
    }
    client = APIClient()
    response = client.post(reverse('token_obtain'), data)
    token = response.data['access']
    client.force_authenticate(user=user, token=token)
    return client


@pytest.fixture
def logged_in_admin_client():
    user = User.objects.create_user(
        username='test1@gmail.com',
        email='test1@gmail.com',
        password='testtesttest',
        is_staff=True,
        is_superuser=True,
        is_active=True
    )
    data = {
        'username': user.username,
        'password': 'testtesttest'
    }
    client = APIClient()
    response = client.post(reverse('token_obtain'), data)
    token = response.data['access']
    client.force_authenticate(user=user, token=token)
    return client


@pytest.fixture
def provider():
    user = User.objects.create_user(
        username='test2@gmail.com',
        email='test2@gmail.com',
        password='testtesttest',
        is_active=True
    )
    provider = Provider.objects.create(
        name='Provider name',
        user=user,
        phone_number='2356635623',
        language='Russian',
        currency='USD'
    )
    return provider


@pytest.fixture
def service_area(provider):
    poly = Polygon(
        [
            [24.301757809117316, 50.51342652114294],
            [25.488281246452164, 49.979487755905694],
            [23.598632809215417, 48.95136646580187],
            [22.895507809313518, 49.58222603945369],
            [23.203124996770768, 49.86631672436136],
            [24.301757809117316, 50.51342652114294]
        ]
    )
    service_area = ServiceArea.objects.create(
        provider=provider,
        name="Area Name",
        price=100.00,
        poly=poly
    )
    return service_area
