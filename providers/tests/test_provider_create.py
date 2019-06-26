import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient
from providers.models import Provider


@pytest.mark.django_db
def test_create_provider():
    client = APIClient()
    data = {
        'user': {
            'password': 'Secret2019',
            'email': 'test@gmail.com'
        },
        'name': 'Test name',
        'phone_number': '6476347637',
        'language': 'English',
        'currency': 'USD'
    }
    response = client.post(reverse('providers-list'), data, format='json')
    assert response.status_code == 201
    created_provider = Provider.objects.get(name=data['name'])
    assert created_provider.phone_number == data['phone_number']
    assert created_provider.language == data['language']
    assert created_provider.currency == data['currency']






