from api.serializers import ReservationSerializer, TableSerializer
from api.viewset import CreateDestroyListViewSet
from reservations.models import Reservation, Table


class ReservationViewSet(CreateDestroyListViewSet):
    """Набор представлений для работы с бронью."""

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TableViewSet(CreateDestroyListViewSet):
    """Набор представлений для работы со столами."""

    queryset = Table.objects.all()
    serializer_class = TableSerializer
