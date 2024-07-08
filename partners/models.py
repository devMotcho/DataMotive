from django.db import models


class Partner(models.Model):
 
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')
    email = models.EmailField(blank=True, null=True,verbose_name='Email')
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone Number')
    address = models.TextField(blank=True, null=True, verbose_name='Address')
    is_client = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f'{self.name}'
