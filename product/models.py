from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

from src.utils import generate_code

class Measurement(models.Model):
    """
    Measurement Units like:
    Unit, Kg, ...
    """
    measure = models.CharField(max_length=100, unique=True, default='Unit', verbose_name='Measure')

    def __str__(self):
        return f'{self.measure}'
    

class Category(models.Model):
    """
    Category Related to Product 1-N ,
    name field should be easy to access and to identify
    """
    name = models.CharField(
        max_length=100, unique=True, default='No Name', verbose_name='Category'
    )
    category_img = models.ImageField(upload_to='category', default='default_img.jpg', blank=True)
    def __str__(self):
        return f'{self.name}'
    
    def product_count(self):
        return self.products.count()
    
    def get_product(self):
        return self.products

class Product(models.Model):
    """
    When created a Product a instance of stock is created
    """
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')
    ref = models.CharField(max_length=18, unique=True, verbose_name='Ref', null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    product_img = models.ImageField(upload_to='product', default='default_img.jpg', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category', related_name='products')
    active = models.BooleanField(default=True,verbose_name='Active')
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True, verbose_name='Measurement', related_name='products')
    price = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, help_text='Value in Euros', verbose_name='Price')
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=0, help_text="%",
                                   validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   verbose_name='Discount', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def final_price(self):
        if self.discount is not None or 0:
            discount_value = (float(self.price) * float(self.discount) * 0.01)
            val = float(self.price) - discount_value
            return round(val, 2)
        return round(Decimal(self.price), 2)
    
    def save(self, *args, **kwargs):
        if self.discount is None or '':
            self.discount = 0
        if self.ref is None or '':
            self.ref = generate_code()
        return super().save(*args, **kwargs)
    
    def get_suppliers(self):
        return self.suppliers
    
    def get_stock(self):
        return self.in_stock
    
    def __str__(self):
        return f'{self.category} - {self.name} ({self.active}) -> {self.final_price} €'