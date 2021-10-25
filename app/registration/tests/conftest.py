import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from registration import models


@pytest.fixture
def api_client():
    return APIClient


@pytest.mark.django_db
@pytest.fixture
def get_vehicle_id():
    vehicle = baker.make(models.Vehicle)

    return vehicle.id
