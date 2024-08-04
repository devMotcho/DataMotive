from transactions.models import Sale, Purchase

def get_sales_by_client(client):
    return Sale.objects.filter(client=client)

def get_purchases_by_supplier(supplier):
    return Purchase.objects.filter(supplier=supplier)