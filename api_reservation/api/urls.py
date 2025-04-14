from django.urls import include, path
from rest_framework import routers

from api.views import ReservationViewSet, TableViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('reservations', ReservationViewSet, basename='reservations')
router_v1.register('tables', TableViewSet, basename='tables')

urlpatterns = [
    path('', include(router_v1.urls)),
]
