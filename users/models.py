from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Класс для описания модели Пользователь"""
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Имя')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='Фамилия')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
