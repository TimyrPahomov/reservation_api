from django.contrib import admin

from reservations.models import Reservation, Table


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Класс для представления броней в Админ-зоне."""

    list_display = (
        'id', 'customer_name', 'table', 'reservation_time', 'duration_minutes'
    )
    search_fields = ('table',)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Класс для представления столиков в Админ-зоне."""

    list_display = ('name', 'seats', 'location')
    search_fields = ('seats',)
