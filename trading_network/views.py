from rest_framework import viewsets
from trading_network.models import Organization, Product, Consignment
from trading_network.serializers import OrganizationSerializer, ProductSerializer, ConsignmentSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью Организация"""
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода create:
        если тип организации - розничная сеть, чек-бокс is_provider = False
        если тип организации - индивидуальный предприниматель, чек-бокс is_provider = True
        """
        organization = serializer.save()
        if organization.type == 'retail':
            organization.is_provider = False
        elif organization.type == 'sole_trader':
            organization.is_provider = True
        organization.save()


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью Продукт"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ConsignmentViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью Накладная"""
    serializer_class = ConsignmentSerializer
    queryset = Consignment.objects.all()

    def perform_update(self, serializer):
        """Переопределение метода update:
        поле total (используется для отражения задолженности перед поставщиком) не доступно для редактирования
        """
        serializer.validated_data.pop('total', None)
        serializer.save()
