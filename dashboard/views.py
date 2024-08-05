from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json


from stock.models import Stock
from .utils import (get_products_count, get_categories_count, 
                    get_clients_count,get_measurements_count, 
                    get_sales_count, get_purchases_count, 
                    get_suppliers_count)
from .kpis import (get_income_of_current_month, top_product,
                   get_expense_of_current_month, get_sales_count_of_current_month,
                   get_purchases_count_of_current_month)

@login_required(login_url='authentic:login')
def homeView(request):

    # Counters for cards
    products_count = get_products_count()
    categories_count = get_categories_count()
    measurements_count = get_measurements_count()
    clients_count = get_clients_count()
    sales_count = get_sales_count()
    purchases_count = get_purchases_count()
    suppliers_count = get_suppliers_count()

    # Stock bar chart
    stocks = list(Stock.objects.values('product__name', 'quantity'))
    stocks_json = json.dumps(stocks)


    # KPI's
    sales_current_month = get_income_of_current_month()
    top1_product = top_product()
    purchases_current_month = get_expense_of_current_month()
    sales_count_current_month = get_sales_count_of_current_month()
    purchases_count_current_month = get_purchases_count_of_current_month




    context = {
        'products_count' : products_count,
        'categories_count' : categories_count,
        'measurements_count' : measurements_count,
        'clients_count' : clients_count,
        'sales_count' : sales_count,
        'purchases_count' : purchases_count,
        'suppliers_count' : suppliers_count,
        'stocks':stocks_json,

        'sales_current_month' : sales_current_month,
        'top_product' : top1_product,
        'purchases_current_month' : purchases_current_month,
        'sales_count_current_month' : sales_count_current_month,
        'purchases_count_current_month' : purchases_count_current_month,
    }
    return render(request, 'dashboard/home.html', context)