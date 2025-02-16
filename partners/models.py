from django.db import models
from django.core.validators import (
    EmailValidator, MinLengthValidator, 
    MaxLengthValidator, RegexValidator,
    validate_image_file_extension)


from product.models import Product
from src.utils import generate_code
from src.validators import validate_names


class EntityType(models.Model):
    """
    Some types of entity like:
    individual, corporate,
    Manufator, Distributor, ....
    """
    entity_type = models.CharField(
        max_length=20, unique=True,
        validators=[validate_names],
        verbose_name='Entity Type'
    )

    def get_clients_count(self):
        return self.clients.count()
    def get_suppliers_count(self):
        return self.suppliers.count()
    
    def __str__(self):
        return f'{self.entity_type}'
    
    class Meta:
        ordering = ['id']


class Partner(models.Model):
    name = models.CharField(
        max_length=255, unique=True,
        validators=[validate_names],
        verbose_name='Name'
    )
    email = models.EmailField(
        blank=True, null=True,
        validators=[EmailValidator], 
        verbose_name='Email'
    )
    contact = models.CharField(
        max_length=20, blank=True, null=True,
        validators=[MinLengthValidator(9), MaxLengthValidator(13)], 
        verbose_name='Phone Number'
    )
    address = models.TextField(
        blank=True, null=True,
        validators=[MaxLengthValidator(300)],
        verbose_name='Address'
    )
    note = models.TextField(
        blank=True, null=True,
        verbose_name='Note'
    )
    active = models.BooleanField(
        default=False, 
        verbose_name='Active'
    )
    partner_logo = models.ImageField(
        upload_to='partner', default='default_img.jpg',
        validators=[validate_image_file_extension],
        verbose_name='Partner Logo', blank=True
    )

    partner_since = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Client(Partner):
    client_id = models.CharField(
        max_length=20, blank=True,
        validators=[RegexValidator],
        verbose_name='Cient ID'
    )
    entity = models.ForeignKey(
        EntityType, on_delete=models.PROTECT,
        null=True, blank=True, verbose_name='Entity Type',
        related_name='clients'
    )

    def save(self, *args, **kwargs):
        if self.client_id == '':
            self.client_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.entity})'
    
    class Meta:
        ordering = ['id']


class Supplier(Partner):
    supplier_id = models.CharField(
        max_length=20, blank=True,
        validators=[RegexValidator], 
        verbose_name='Supplier ID'
    )
    products = models.ManyToManyField(
        Product, verbose_name='Products',
        related_name='suppliers'
    )
    entity = models.ForeignKey(
        EntityType, on_delete=models.PROTECT,
        null=True, blank=True, verbose_name='Entity Type', 
        related_name='suppliers'
    )

    def save(self, *args, **kwargs):
        if self.supplier_id == '':
            self.supplier_id = generate_code()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name} ({self.entity})'

    class Meta:
        ordering = ['id']
