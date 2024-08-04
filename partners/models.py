from django.db import models


from product.models import Product
from src.utils import generate_code

class EntityType(models.Model):
    """
    Some types of entity like:
    individual, corporate,
    Manufator, Distributor, ....
    """
    entity_type = models.CharField(max_length=20, unique=True, verbose_name='Entity Type')

    def get_clients_count(self):
        return self.clients.count()
    def get_suppliers_count(self):
        return self.suppliers.count()
    
    def __str__(self):
        return f'{self.entity_type}'
    
    class Meta:
        ordering = ['id']


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
    client_id = models.CharField(max_length=20, blank=True, verbose_name='Cient ID')
    entity = models.ForeignKey(EntityType, on_delete=models.PROTECT, null=True, blank=True, related_name='clients', verbose_name='Entity Type')

    def save(self, *args, **kwargs):
        if self.client_id == '':
            self.client_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.entity}) - {self.email}'
    
    class Meta:
        ordering = ['id']


class Supplier(Partner):
    supplier_id = models.CharField(max_length=20, blank=True, verbose_name='Supplier ID')
    products = models.ManyToManyField(Product, related_name='suppliers', verbose_name='Products')
    entity = models.ForeignKey(EntityType, on_delete=models.PROTECT, null=True, blank=True, related_name='suppliers', verbose_name='Entity Type')

    
    def save(self, *args, **kwargs):
        if self.supplier_id == '':
            self.supplier_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.entity}) - {self.email}'

    class Meta:
        ordering = ['id']
