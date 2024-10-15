from django.db import models
from decimal import Decimal
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone 

from src.settings import IS_PRODUCTION
from product.models import Product


class Stock(models.Model):
    """
    A Stock instance is created when a product is, with a quantity = 0
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_stock')
    quantity = models.IntegerField(verbose_name='Quantity')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    @property
    def value(self):
        """
        Monetary Value of the stocked products
        """
        result = Decimal(float(self.quantity) * float(self.product.final_price))
        return round(result, 2)


    def save(self, *args, **kwargs):
        if not IS_PRODUCTION:
            if self.quantity is not None:
                self.quantity
            else:
                self.quantity = 0
            
            if self.created == '':
                self.created = timezone.now()

            return super().save(*args, **kwargs)
        return
    
    def delete(self):
        if not IS_PRODUCTION:
            return super().delete()
        return
    def __str__(self):
        return f'{self.product.name} - {self.quantity} in stock ({self.value}€)'
    
    class Meta:
        ordering = ['id']



@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, *args, **kwargs):
    if created:
        Stock.objects.create(product=instance, quantity=0)
