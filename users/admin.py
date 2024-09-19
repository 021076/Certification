from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для модели Пользователь"""
    list_display = ('last_name', 'first_name', 'phone', 'email', 'is_active')
