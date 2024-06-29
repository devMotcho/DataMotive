from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Measurement(models.TextChoices):
    """
    Measurement Units
    """
    UNI = 'Unit' # Product Sale by Unit
    KG = 'Kg' # Product Sale By Weight
    

class Category(models.Model):
    """
    Primary Category Related to Product,
    Name must be easy to access and to identify
    """
    name = models.CharField(
        max_length=100, unique=True, default='No Name', verbose_name='Category'
    )
    #category_img
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    """
    Products related to Sales
    """
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    product_img = models.ImageField(upload_to='product', default='default_img.jpg')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Category')
    active = models.BooleanField(default=True,verbose_name='Active')
    measurement = models.CharField(max_length=4, choices=Measurement.choices, default=Measurement.UNI, verbose_name='Measurement')
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, help_text='Value in Euros', verbose_name='Price')
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=0, help_text="%",
                                   validators=[MinValueValidator(0), MaxValueValidator(100)],
                                   verbose_name='Discount')
    
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
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.category} - {self.name} ({self.active}) -> {self.final_price} €'
