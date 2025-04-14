from rest_framework import serializers

from reservations.models import Reservation, Table
from utils.functions import validate_date, validate_reservation_time


class ReservationSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с бронью."""

    reservation_time = serializers.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M']
    )

    class Meta:
        model = Reservation
        fields = (
            'id',
            'customer_name',
            'table',
            'reservation_time',
            'duration_minutes'
        )

    def validate(self, data):
        """Проверяет бронь на корректность заполнения."""
        reservation_time = data.get('reservation_time')
        duration_minutes = data.get('duration_minutes')
        table = data.get('table')
        validate_date(reservation_time)
        validate_reservation_time(
            duration_minutes, reservation_time, table, Reservation
        )
        return data


class TableSerializer(serializers.ModelSerializer):
    """Сериализатор для работы со столами."""

    class Meta:
        model = Table
        fields = ('id', 'name', 'seats', 'location')
