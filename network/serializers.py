from rest_framework.serializers import IntegerField, ModelSerializer

from network.models import Network, Product


class ProductSerializer(ModelSerializer):
    """Сериализатор продукта"""

    class Meta:
        model = Product
        fields = ["id", "name", "model", "data", "network"]


class NetWorkSerializer(ModelSerializer):
    """Сериализатор узла сети"""

    product = ProductSerializer(many=True, read_only=True)
    level = IntegerField(source="get_level", read_only=True)

    class Meta:
        model = Network
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "debt_to_supplier",
            "date_created",
            "get_level",
            "product",
        ]
        read_only_fields = ["debt_to_supplier"]
