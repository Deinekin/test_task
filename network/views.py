from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from network.models import Network
from network.permissions import UserIsActive
from network.serializers import NetWorkSerializer


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetWorkSerializer
    permission_classes = [UserIsActive]

    filter_backends = [DjangoFilterBackend]
    filter_fields = ["country"]
