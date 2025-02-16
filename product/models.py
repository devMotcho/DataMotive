from decimal import Decimal
from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator,
    RegexValidator, MaxLengthValidator,
    DecimalValidator, validate_image_file_extension
)

from .validators import validate_unit_of_measure
from src.utils import generate_code
from src.validators import validate_names


class Measurement(models.Model):

    measure = models.CharField(
        max_length=100, unique=True, default='Unit',
        validators=[validate_unit_of_measure], 
        verbose_name='Measure'
    )

    def __str__(self):
        return f'{self.measure}'
    

class Category(models.Model):

    name = models.CharField(
        max_length=100, unique=True, default='No Name',
        validators=[validate_names],
        verbose_name='Category'
    )
    category_img = models.ImageField(
        upload_to='category', default='default_img.jpg', 
        validators=[validate_image_file_extension],
        verbose_name='Category Image', blank=True
    )

    def __str__(self):
        return f'{self.name}'
    
    def product_count(self):
        return self.products.count()
    
    def get_product(self):
        return self.products.all()

class Product(models.Model):

    name = models.CharField(
        max_length=120, unique=True,
        validators=[validate_names],
        verbose_name='Name'
    )
    ref = models.CharField(
        max_length=18, unique=True,
        validators=[RegexValidator],
        verbose_name='Ref', null=True, blank=True
    )
    description = models.TextField(
        blank=True, null=True,
        validators=[MaxLengthValidator(1000)],
        verbose_name='Description'
    )
    product_img = models.ImageField(
        upload_to='product', default='default_img.jpg',
        validators=[validate_image_file_extension],
        verbose_name='Product Image', blank=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        verbose_name='Category', null=True,
        related_name='products'
    )
    active = models.BooleanField(
        default=True,verbose_name='Active'
    )
    measurement = models.ForeignKey(
        Measurement, on_delete=models.SET_NULL,
        verbose_name='Measurement', null=True,
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=18, decimal_places=2, default=0.00,
        help_text='Value in Euros',
        validators=[DecimalValidator(18, 2)],
        verbose_name='Price'
    )
    discount = models.DecimalField(
        max_digits=3, decimal_places=0, default=0, help_text="%",
        validators=[MinValueValidator(0), MaxValueValidator(100), DecimalValidator(3, 0)],
        verbose_name='Discount', blank=True
    )

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
        return self.suppliers.all()
    
    def get_stock_quantity(self):
        return self.in_stock.quantity
    
    def __str__(self):
        return f'{self.name} [{self.category}] ({self.final_price}€)'
    
    class Meta:
        ordering = ['id']
