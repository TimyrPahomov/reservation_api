from http import HTTPStatus

import pytest

from reservations.models import Reservation, Table


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    (
        '/api/tables/',
        '/api/reservations/',
    ),
)
def test_pages_availability(client, name):
    url = name
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_user_can_create_table(client, table_data, table_url):
    response = client.post(table_url, data=table_data)
    assert response.status_code == HTTPStatus.CREATED
    tables_count = Table.objects.count()
    assert tables_count == 1


@pytest.mark.django_db
def test_user_can_delete_table(client, table, table_url):
    client.delete(f'{table_url}{table.id}/')
    comments_count = Table.objects.count()
    assert comments_count == 0


@pytest.mark.django_db
def test_user_can_create_reservation(
    client, reservation_data, reservation_url
):
    response = client.post(reservation_url, data=reservation_data)
    assert response.status_code == HTTPStatus.CREATED
    reservations_count = Reservation.objects.count()
    assert reservations_count == 1


@pytest.mark.django_db
def test_user_can_delete_reservation(client, reservation, reservation_url):
    client.delete(f'{reservation_url}{reservation.id}/')
    comments_count = Reservation.objects.count()
    assert comments_count == 0


@pytest.mark.django_db
def test_user_cant_reservation_reserved_table(
    client, reservation_url, reservation, reservation_test_data
):
    for data in reservation_test_data:
        response = client.post(reservation_url, data=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.django_db
def test_user_cant_reservation_past_date(client, reservation_url, table_id):
    data = {
        'customer_name': 'Клиент №3',
        'table': table_id,
        'reservation_time': '2024-04-14 16:30',
        'duration_minutes': 60
    }
    response = client.post(reservation_url, data=data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
