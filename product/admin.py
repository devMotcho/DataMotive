from django.contrib import admin
from .models import Category, Product, Measurement
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Measurement)