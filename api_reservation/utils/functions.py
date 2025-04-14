from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.timezone import now, pytz

from utils.constants import SECONDS_IN_MINUTE


def get_timezone(datetime):
    """Получает текущий часовой пояс."""
    return datetime.astimezone(pytz.timezone(settings.TIME_ZONE))


def validate_date(value):
    """
    Проверяет, что дата и время бронирования не раньше текущих даты и времени.
    """
    current_time = get_timezone(now())
    delta = value - current_time
    if delta.total_seconds() < 0:
        raise ValidationError(
            'Бронирование не может быть раньше текущих даты и времени.'
        )


def validate_reservation_time(
        duration_minutes, reservation_time, table, model
):
    """
    Проверяет допустимость даты и времени бронирования.

    Нельзя забронировать стол на уже забронированное время.
    """
    duration_seconds = duration_minutes * SECONDS_IN_MINUTE
    reservation_time = reservation_time.timestamp()
    end_of_reservation_time = (
        reservation_time + duration_seconds
    )
    table_reservations = model.objects.filter(table=table)
    for reservation in table_reservations:
        beginning_of_table_reservation = (
            reservation.reservation_time.timestamp()
        )
        table_reservation_duration = (
            reservation.duration_minutes * SECONDS_IN_MINUTE
        )
        end_of_table_reservation = (
            beginning_of_table_reservation + table_reservation_duration
        )
        if (
            beginning_of_table_reservation
            <= reservation_time <= end_of_table_reservation
        ):
            raise ValidationError(
                'Столик уже забронирован на данное время'
            )
        if (
            reservation_time <= beginning_of_table_reservation
            <= end_of_reservation_time
        ):
            raise ValidationError(
                'Невозможно забронировать столик на данный период времени,'
                ' выберите другую продолжительность бронирования.'
            )
