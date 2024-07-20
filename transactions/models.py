from django.db import models
from django.utils import timezone

from product.models import Product
from partners.models import Client, Supplier
from src.utils import generate_code

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=12, primary_key=True, blank=True , unique=True, verbose_name='Transaction ID')
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Product')
    note = models.TextField(blank=True, verbose_name='Note')
    transaction_date = models.DateField(verbose_name='Transaction Date')

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.transaction_id == '':
            self.transaction_id = generate_code()
        if self.created == '':
            self.created = timezone.now
        if self.updated == '':
            self.updated = timezone.now
        
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ['-transaction_date']


class Sale(Transaction):
    """
    Sale of Products to Clients
    """
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='sales', verbose_name='Client')

    @property
    def final_price(self):
        if self.quantity is None:
            result = 0
            return result
        else:
            result = float(self.quantity) * float(self.product.final_price)
            return round(result, 2)
    

    def __str__(self):
        return f'{self.transaction_id} - {self.quantity} x of product {self.product} at {self.final_price} €'
    

    
class Purchase(Transaction):
    """
    Purchase Products from Suppliers
    """
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='purchases', verbose_name='Supplier')
    final_price = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text="Value in Euros", verbose_name="Final Price")

    
    def __str__(self):
        return f'{self.transaction_id} - {self.quantity} x of product {self.product} at {self.final_price} €'
    
