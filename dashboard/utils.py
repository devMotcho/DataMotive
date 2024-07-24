from product.models import Product, Category, Measurement
from partners.models import Supplier, Client
from transactions.models import Sale, Purchase

def get_products_count():
    products = Product.objects.all()
    return products.count

def get_categories_count():
    categories = Category.objects.all()
    return categories.count

def get_measurements_count():
    measurements = Measurement.objects.all()
    return measurements.count

def get_suppliers_count():
    suppliers = Supplier.objects.all()
    return suppliers.count

def get_clients_count():
    clients = Client.objects.all()
    return clients.count

def get_sales_count():
    sales = Sale.objects.all()
    return sales.count

def get_purchases_count():
    purchases = Purchase.objects.all()
    return purchases.count