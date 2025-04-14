from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import RestaurantUser


@admin.register(RestaurantUser)
class RestaurantUserAdmin(UserAdmin):
    """Админ-зона Пользователей."""

    model = RestaurantUser
    list_display = ('username',)
