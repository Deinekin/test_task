from django.db import models

NULLABLE = {"blank": True, "null": True}


class Network(models.Model):
    """Модель данных узла сети"""

    name = models.CharField(max_length=50, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    supplier = models.ForeignKey("self", on_delete=models.SET_NULL, **NULLABLE)
    debt_to_supplier = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Долг перед поставщиком"
    )
    date_created = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    def get_level(self):
        default_level = 0
        node = self.supplier
        while node:
            default_level += 1
            node = node.supplier
        return default_level

    def __str__(self):
        return f"{self.name}, {self.email}: {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"


class Product(models.Model):
    """Модель продукта"""

    name = models.CharField(max_length=50, verbose_name="Название")
    model = models.CharField(max_length=50, verbose_name="Модель")
    data = models.DateField(verbose_name="Дата выпуска")

    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name="Узел")

    def __str__(self):
        return f"{self.name}, {self.model}, {self.data} - {self.network}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
