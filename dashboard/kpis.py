from transactions.models import Sale, Purchase
from datetime import datetime
from django.db.models import Sum

now = datetime.now()
current_year = now.year
current_month = now.month

def get_income_of_current_month():

    #Filter sales for the current month
    sales = Sale.objects.filter(
        transaction_date__year=current_year,
        transaction_date__month=current_month
    )

    income = 0
 
    for sale in sales:
        income += sale.final_price
    
    return income

def get_expense_of_current_month():

    purchases = Purchase.objects.filter(
        transaction_date__year=current_year,
        transaction_date__month=current_month
    )

    expenses = 0

    for purchase in purchases:
        expenses += purchase.final_price
    
    return expenses


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