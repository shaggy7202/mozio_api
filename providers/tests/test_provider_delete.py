import pytest

from django.shortcuts import reverse
from rest_framework.test import APIClient

from providers.models import Provider


@pytest.mark.django_db
def test_provider_delete(provider):
    pk = provider.pk
    client = APIClient()
    client.force_authenticate(user=provider.user)
    response = client.delete(reverse(
        'providers-detail',
        args=(pk,)
    ))
    assert response.status_code == 204
    assert not Provider.objects.filter(pk=pk).exists()


@pytest.mark.django_db
def test_login_required(provider):
    client = APIClient()
    response = client.delete(reverse('providers-detail', args=(provider.pk,)))
    assert response.status_code == 401


@pytest.mark.django_db
def test_available_for_admin(logged_in_admin_client, provider):
    response = logged_in_admin_client.delete(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 204


@pytest.mark.django_db
def test_not_available_for_other_provider(logged_in_client, provider):
    response = logged_in_client.delete(reverse(
        'providers-detail',
        args=(provider.pk,)
    ))
    assert response.status_code == 403
