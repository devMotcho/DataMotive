from django.db import models
from decimal import Decimal

from product.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_stock')
    quantity = models.IntegerField(verbose_name='Quantity')
    
    updated = models.DateTimeField(auto_now=True)

    @property
    def value(self):
        """
        Value of the stocked products
        """
        return Decimal(float(self.quantity) * float(self.product.final_price))

    def __str__(self):
        return f'{self.product.name} - {self.quantity} in stock ({self.value}€)'
    