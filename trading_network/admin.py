from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from trading_network.models import Organization, Product, Consignment


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Админка для модели Организация"""
    list_display = ('title', 'email', 'country', 'city', 'type', 'is_provider',)
    list_filter = ('city', 'country')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для модели Продукт"""
    list_display = ('title', 'brand', 'market_entry',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.action(description="Убрать задолженность перед поставщиком")
def no_debt(self, request, queryset):
    """Admin action, очищающий задолженность перед поставщиком у выбранных объектов"""
    queryset.update(is_paid=True)


@admin.register(Consignment)
class ConsignmentAdmin(admin.ModelAdmin):
    """Админка для модели Накладная"""
    list_display = ('uuid', 'product_link', 'retail_link', 'provider_link', 'debt',)
    actions = [no_debt]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Фильтрация выпадающих списков для выбора розничной сети и поставщика"""
        if db_field.name == "provider":
            kwargs["queryset"] = Organization.objects.filter(is_provider=True)
        elif db_field.name == "retail":
            kwargs["queryset"] = Organization.objects.filter(type='retail')
        return super(ConsignmentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def product_link(self, obj):
        """Открытие по ссылке информации о товаре"""
        url = reverse("admin:trading_network_product_change", args=[obj.product.pk])
        link = '<a href="%s">%s</a>' % (url, obj.product)
        return mark_safe(link)

    product_link.short_description = 'Товар'

    def retail_link(self, obj):
        """Открытие по ссылке информации о розничной сети"""
        url = reverse("admin:trading_network_organization_change", args=[obj.retail.pk])
        link = '<a href="%s">%s</a>' % (url, obj.retail)
        return mark_safe(link)

    retail_link.short_description = 'Розничная сеть(магазин)'

    def provider_link(self, obj):
        """Открытие по ссылке информации о поставщике"""
        url = reverse("admin:trading_network_organization_change", args=[obj.provider.pk])
        link = '<a href="%s">%s</a>' % (url, obj.provider)
        return mark_safe(link)

    provider_link.short_description = 'Поставщик'

    def debt(self, obj):
        """Отражение информации о задолженности перед поставщиком"""
        if not obj.is_paid:
            return obj.total
        else:
            return 'Нет'

    debt.short_description = 'Задолженность перед поставщиком'
