from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import NetworkViewSet

app_name = NetworkConfig.name

router = SimpleRouter()
router.register("", NetworkViewSet)

urlpatterns = []

urlpatterns += router.urls
