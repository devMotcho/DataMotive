from django.db import models
from decimal import Decimal
from django.dispatch import receiver
from django.db.models.signals import post_save

from product.models import Product


class Stock(models.Model):
    """
    A Stock instance is created when a product is, with a quantity = 0
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_stock')
    quantity = models.IntegerField(verbose_name='Quantity')
    
    updated = models.DateTimeField(auto_now=True)

    @property
    def value(self):
        """
        Monetary Value of the stocked products
        """
        return Decimal(float(self.quantity) * float(self.product.final_price))

    def save(self, *args, **kwargs):
        if self.quantity is not None:
            self.quantity
        else:
            self.quantity = 0
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} - {self.quantity} in stock ({self.value}€)'

@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, *args, **kwargs):
    if created:
        Stock.objects.create(product=instance, quantity=0)