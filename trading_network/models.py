import uuid
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Organization(models.Model):
    """Класс для описания модели Организация"""
    TYPE_ORG = (('factory', 'factory'), ('retail', 'retail'), ('sole_trader', 'sole_trader'))
    objects = None
    title = models.CharField(max_length=150, verbose_name='Название')
    type = models.CharField(max_length=20, choices=TYPE_ORG, verbose_name='Тип')
    is_provider = models.BooleanField(default=False, verbose_name='Признак поставщика')
    email = models.EmailField(unique=True, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house = models.CharField(max_length=150, verbose_name='Номер дома')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Торговая сеть'


class Product(models.Model):
    """Класс для описания модели Продукт"""
    objects = None
    title = models.CharField(max_length=150, verbose_name='Название товара')
    brand = models.TextField(verbose_name='Модель товара')
    market_entry = models.DateField(verbose_name='Дата выхода на рынок')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Склад'


class Consignment(models.Model):
    """Класс для описания модели Накладная"""
    objects = None
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='ID накладной')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    retail = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='retail',
                               verbose_name='Розничная сеть')
    provider = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='provider',
                                 verbose_name='Поставщик')
    unit_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена за единицу')
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма к оплате')
    is_ship = models.BooleanField(default=False, verbose_name='Признак отгрузки товара')
    is_paid = models.BooleanField(default=False, verbose_name='Признак оплаты товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return f'{self.product}, {self.retail}, {self.provider}'

    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Товарная ведомость'
