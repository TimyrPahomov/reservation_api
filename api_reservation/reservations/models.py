from django.core.validators import MinValueValidator
from django.db import models

from utils.constants import (
    INVALID_SEATS_MESSAGE,
    MIN_SEATS,
    RESERVATION_CUSTOMER_NAME_MAX_LENGTH,
    TABLE_LOCATION_MAX_LENGTH,
    TABLE_NAME_MAX_LENGTH
)
from utils.functions import (
    get_timezone,
    validate_date,
    validate_reservation_time
)


class Table(models.Model):
    """Модель столика."""

    name = models.CharField(
        'Название',
        unique=True,
        max_length=TABLE_NAME_MAX_LENGTH,
    )
    seats = models.PositiveSmallIntegerField(
        'Количество мест',
        validators=(
            MinValueValidator(
                MIN_SEATS, message=INVALID_SEATS_MESSAGE
            ),
        )
    )
    location = models.CharField(
        'Местоположение',
        max_length=TABLE_LOCATION_MAX_LENGTH,
    )
    created_at = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'стол'
        verbose_name_plural = 'Столы'

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """Модель бронирования."""

    customer_name = models.CharField(
        'Имя клиента',
        max_length=RESERVATION_CUSTOMER_NAME_MAX_LENGTH,
    )
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE,
        verbose_name='Столик',
    )
    reservation_time = models.DateTimeField(
        'Время бронирования',
        unique=True,
        validators=(validate_date,)
    )
    duration_minutes = models.PositiveSmallIntegerField(
        'Длительность брони в минутах'
    )
    created_at = models.DateTimeField('Время создания', auto_now_add=True)

    class Meta:
        default_related_name = 'reservations'
        verbose_name = 'бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return (
            f'{self.table.name} забронирован {self.customer_name} '
            f'на дату {get_timezone(self.reservation_time)}'
        )

    def clean(self):
        validate_reservation_time(
            self.duration_minutes,
            self.reservation_time,
            self.table,
            Reservation
        )
