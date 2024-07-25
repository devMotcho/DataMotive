from transactions.models import Sale
from .models import Client

def get_sales_by_client(client):
    return Sale.objects.filter(client=client)
