from django.db import models
from myshop import settings
from product_app.models import Product


# Модель корзины покупок
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity} - {self.add_datetime}'

    @property
    def product_price(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    @property
    def total_price(self):
        _items = Basket.objects.filter(user=self.user)
        _totalprice = sum(list(map(lambda x: x.product_price, _items)))
        return _totalprice
