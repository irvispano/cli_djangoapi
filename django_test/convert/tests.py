# from django.test import TestCase

# Create your tests here.
from django.test import client
import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


def test_convert(client):
    """
    Test convert url
    """
    url = reverse("convert")
    response = client.get(url)
    assert response.status_code == 417


def test_convert_url_amount_param(client):
    """
    Test convert url with amount param"""
    url = reverse("convert")
    response = client.get(
        url, data={"amount": 100, "from_currency": "USD", "to_currency": "EUR"}
    )
    print(response.json())
    assert response.status_code == 200
