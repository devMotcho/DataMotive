from transactions.models import Purchase, Sale
from .models import Product

def get_purchases_by_product(product):
    return Purchase.objects.filter(product=product)

def get_sales_by_product(product):
    return Sale.objects.filter(product=product)

def get_products_by_category(category):
    return Product.objects.filter(category=category)