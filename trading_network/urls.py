from rest_framework import routers
from trading_network.apps import TradingNetworkConfig
from trading_network.views import OrganizationViewSet, ProductViewSet, ConsignmentViewSet

app_name = TradingNetworkConfig.name

router = routers.DefaultRouter()
router.register(r'organization', OrganizationViewSet, 'organization')
router.register(r'product', ProductViewSet, 'product')
router.register(r'consignment', ConsignmentViewSet, 'consignment')

urlpatterns = router.urls
