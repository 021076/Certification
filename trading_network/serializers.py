from rest_framework import serializers
from trading_network.models import Organization, Product, Consignment


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Организации"""

    class Meta:
        model = Organization
        fields = '__all__'

    def validate(self, data, null=None):
        if data['type'] == 'sole_trader' and not data['is_provider']:
            raise serializers.ValidationError(
                'Если тип организации ИП, то должен быть признак поставщика')
        elif data['type'] == 'retail' and data['is_provider']:
            raise serializers.ValidationError('Розничная сеть не может быть поставщиком')
        return data


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Продукт"""

    class Meta:
        model = Product
        fields = '__all__'


class ConsignmentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с контроллером создания Накладаная"""

    class Meta:
        model = Consignment
        fields = '__all__'
