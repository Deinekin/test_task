from django.contrib import admin

from network.models import Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Админ-панель сети"""

    list_display = (
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
        "supplier_link",
    )
    list_filter = ("city",)
    search_fields = (
        "name",
        "city",
    )
    actions = [
        "clear_debt",
    ]

    def get_level(self, obj):
        """Уровень иерархии"""

        return obj.get_level()

    get_level.short_description = "Уровень узла сети"

    def supplier_link(self, obj):
        """Ссылка на поставщика"""

        if not obj.supplier:
            return "Нет данных поставщика"

    supplier_link.allow_tags = True

    def clear_debt(self, request, queryset):
        """Очистка долга перед поставщиком"""

        queryset.update(debt_to_supplier=0.00)

    clear_debt.short_description = "Очистить долг перед поставщиком"


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    """Админ-панель продукта"""

    list_display = ("id", "name", "model", "data")
    search_fields = (
        "name",
        "model",
    )
