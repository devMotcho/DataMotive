from django.shortcuts import render
from .utils import (get_products_count, get_categories_count, 
                    get_clients_count,get_measurements_count, 
                    get_sales_count, get_purchases_count, 
                    get_suppliers_count)
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentic:login')
def homeView(request):
    products_count = get_products_count()
    categories_count = get_categories_count()
    measurements_count = get_measurements_count()
    clients_count = get_clients_count()
    sales_count = get_sales_count()
    purchases_count = get_purchases_count()
    suppliers_count = get_suppliers_count()


    context = {
        'products_count' : products_count,
        'categories_count' : categories_count,
        'measurements_count' : measurements_count,
        'clients_count' : clients_count,
        'sales_count' : sales_count,
        'purchases_count' : purchases_count,
        'suppliers_count' : suppliers_count,
    }
    return render(request, 'dashboard/home.html', context)