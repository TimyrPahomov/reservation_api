import pytest

from reservations.models import Reservation, Table


@pytest.fixture
def table():
    return Table.objects.create(
        name='Стол №1',
        seats=2,
        location='Возле окна'
    )


@pytest.fixture
def table_id(table):
    return table.id


@pytest.fixture
def reservation(table):
    return Reservation.objects.create(
        customer_name='Клиент №1',
        table=table,
        reservation_time='3025-07-24 10:00',
        duration_minutes=120
    )


@pytest.fixture
def table_data():
    return {
        'name': 'Стол №2',
        'seats': 4,
        'location': 'По центру',
    }


@pytest.fixture
def reservation_data(table_id):
    return {
        'customer_name': 'Клиент №2',
        'table': table_id,
        'reservation_time': '3025-04-14 16:30',
        'duration_minutes': 60
    }


@pytest.fixture
def table_url():
    return '/api/tables/'


@pytest.fixture
def reservation_url():
    return '/api/reservations/'


@pytest.fixture
def reservation_test_data(table):
    return [
        {
            'customer_name': 'Клиент №3',
            'table': table.id,
            'reservation_time': '3025-07-24 10:00',
            'duration_minutes': 60
        },
        {
            'customer_name': 'Клиент №3',
            'table': table.id,
            'reservation_time': '3025-07-24 10:30',
            'duration_minutes': 60
        },
        {
            'customer_name': 'Клиент №3',
            'table': table.id,
            'reservation_time': '3025-07-24 09:30',
            'duration_minutes': 60
        }
    ]
