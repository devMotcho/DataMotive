from django.db import models


from product.models import Product
from product.utils import generate_code

class ClientType(models.Model):
    """
    individual, corporate, ....
    """
    type = models.CharField(max_length=20)

    def get_clients(self):
        return self.clients

    def __str__(self):
        return f'{self.type}'
    
class SupplierType(models.Model):
    """
    Manufacter, Distributor, ....
    """
    type = models.CharField(max_length=20)

    def get_suppliers(self):
        return self.suppliers

    def __str__(self):
        return f'{self.type}'

class Partner(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    contact = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number')
    address = models.TextField(blank=True, null=True, verbose_name='Address')
    note = models.TextField(blank=True, null=True, verbose_name='Note')
    active = models.BooleanField(verbose_name='Active', default=False)
    partner_logo = models.ImageField(upload_to='partner', default='default_img.jpg', blank=True)

    partner_since = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Client(Partner):
    client_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Cient ID')
    client_type = models.ForeignKey(ClientType, on_delete=models.PROTECT, related_name="clients" ,verbose_name='Client Type')

    def save(self, *args, **kwargs):
        if self.client_id == "" or None:
            self.client_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.client_type}) - {self.email}'


class Supplier(Partner):
    supplier_id = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name='Supplier ID')
    supplier_type = models.ForeignKey(SupplierType, on_delete=models.PROTECT, related_name="suppliers" ,verbose_name='Supplier Type')
    products = models.ManyToManyField(Product, related_name='suppliers', verbose_name='Products')

    
    def save(self, *args, **kwargs):
        if self.supplier_id == "" or None:
            self.supplier_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.supplier_type}) - {self.email}'
