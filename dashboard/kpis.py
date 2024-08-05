from transactions.models import Sale, Purchase
from datetime import datetime
from django.db.models import Sum, Count

now = datetime.now()
current_year = now.year
current_month = now.month


# Sales
def get_sales_current_month():
    #Filter sales for the current month
    return Sale.objects.filter(
        transaction_date__year=current_year,
        transaction_date__month=current_month
    )

def get_income_of_current_month():
    sales = get_sales_current_month()

    income = 0
 
    for sale in sales:
        income += sale.final_price
    
    return income

def get_sales_count_of_current_month():
    return get_sales_current_month().count()


# Purchases
def get_purchases_current_month():
    return Purchase.objects.filter(
        transaction_date__year=current_year,
        transaction_date__month=current_month
    )

def get_expense_of_current_month():

    purchases = get_purchases_current_month()

    expenses = 0

    for purchase in purchases:
        expenses += purchase.final_price
    
    return expenses


def get_purchases_count_of_current_month():
    return get_purchases_current_month().count()


# Products Sales
def top_products(max_value):
    return Sale.objects.filter(transaction_date__year=current_year, transaction_date__month=current_month)\
                               .values('product__name')\
                               .annotate(total_quantity=Sum('quantity'))\
                               .order_by('-total_quantity')[:max_value]

def top_product():
    return Sale.objects.filter(transaction_date__year=current_year, transaction_date__month=current_month)\
                              .values('product__name')\
                              .annotate(total_quantity=Sum('quantity'))\
                              .order_by('-total_quantity')\
                              .first()