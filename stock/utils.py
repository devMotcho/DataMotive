from .models import Stock

def get_stock_by_product(product):
    return Stock.objects.get(product=product)