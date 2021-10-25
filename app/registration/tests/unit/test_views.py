import pytest
from model_bakery import baker

from registration import models


@pytest.mark.django_db
def test_success_get_vehicles_list(api_client):
    count = 3
    baker.make(models.Vehicle, _quantity=count)
    response = api_client().get('/registration/vehicles/')
    assert response.status_code == 200
    assert len(response.data) == count

@pytest.mark.django_db
def test_success_get_vehicles(api_client):
    number = 'А777АА77'
    vehicle = baker.make(models.Vehicle, number=number)
    response = api_client().get(f'/registration/vehicles/{vehicle.id}/')
    assert response.status_code == 200
    assert response.data['number'] == number

@pytest.mark.django_db
def test_success_create_register(api_client):
    vehicle_number = 'А777АА77'

    response = api_client().post(
        '/registration/registration/',
        data={'vehicle_number': vehicle_number + '*А'}
    )

    assert response.status_code == 200
    vehicle = models.Vehicle.objects.first()
    assert vehicle.number == vehicle_number

@pytest.mark.django_db
def test_success_update_category_register(api_client):
    change_category = 'В'
    vehicle_number = 'А777АА77'
    category = models.Category.objects.get(name='А')
    vehicle = baker.make(models.Vehicle, number=vehicle_number, category=category)

    response = api_client().post(
        '/registration/registration/',
        data={'vehicle_number': vehicle_number + f'*{change_category}'}
    )

    vehicle = models.Vehicle.objects.first()
    assert vehicle.category.name == change_category

@pytest.mark.django_db
def test_success_create_to_cyrillic_register(api_client):
    vehicle_number = 'A777AA77' #англ.

    response = api_client().post(
        '/registration/registration/',
        data={'vehicle_number': vehicle_number + '*А'}
    )

    assert response.status_code == 200
    vehicle = models.Vehicle.objects.first()
    assert vehicle.number == 'А777АА77' #рус.

@pytest.mark.django_db
def test_error_format_number_register(api_client):
    errors = (
        {'message': 'Неверный формат номера с категор', 'number': 'А777АА77'},
        {'message': 'Ошибка валидации:', 'number': 'А777АА77*Г'},
        {'message': 'Ошибка валидации:', 'number': 'А777АА7*А'},
        {
            'message': 'Ошибка валидации: Передан недопустимый символ', 
            'number': 'R777АА7*А'
        },
    )

    for _error in errors:
        response = api_client().post(
            '/registration/registration/',
            data={'vehicle_number': _error['number']}
        )

        assert response.data['message'].startswith(_error['message'])
