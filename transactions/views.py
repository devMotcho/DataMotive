from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from transactions.models import Purchase, Sale
from transactions.forms import PurchaseForm, SaleForm
from .utils import (add_to_stock, remove_stock, mirrow_modifications_purchase,
                    mirrow_modifications_sale, calc_profit_on_sale)
from src.utils import get_page_obj

@login_required(login_url='authentic:login')
def purchaseTable(request):
    """
    View Purchases,
    Contains a table with all purchases,
    Search on Navbar by: transaction_id, name, note
    Possibility to create new purchase,
    when a new purchase is created the quantity is added to the stock
    by the add_to_stock function
    """

    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    purchases = Purchase.objects.filter(
        Q(transaction_id__icontains=q) |
        Q(product__name__icontains=q) |
        Q(note__icontains=q)
    )
    page_obj = get_page_obj(purchases, request)

    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            
            add_to_stock(purchase)
            
            messages.success(request, "Purchase Added.")
            return redirect('transactions:purchases')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs' : purchases,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'transactions/purchase/table.html', context)

@login_required(login_url='authentic:login')
def purchaseDetail(request, pk):
    """
    Detail view of a purchased transaction,
    Possibility to update purchase,
    Calculation of sale price,
    Calculation of profit with calc_profit_on_sale
    mirrow_modification function deals with the logic behind updating a purchase instance
    """
    purchase = get_object_or_404(Purchase, transaction_id=pk)

    old_purchase_product = purchase.product
    old_purchase_quantity = purchase.quantity


    sold_product_for = round(float(purchase.product.final_price) * float(purchase.quantity), 2)
    profit_on_sale = calc_profit_on_sale(purchase)
    


    form = PurchaseForm(instance=purchase)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            new_purchase = form.save(commit=False)

            mirrow_modifications_purchase(new_purchase, old_purchase_product, old_purchase_quantity)

            new_purchase.save()
            messages.success(request, "Purchase Updated.")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj' : purchase,
        'form' : form,
        'profit':profit_on_sale,
        'sold_product_for':sold_product_for,
    }
    return render(request, 'transactions/purchase/detail.html', context)

@login_required(login_url='authentic:login')
def purchaseDelete(request, pk):
    """
    Delete Purchase,
    When success the quantity purchased is removed from stock instance
    remove_stock function is called
    """
    purchase = get_object_or_404(Purchase, transaction_id=pk)
    if request.method == 'POST':
        purchase.delete()
        messages.success(request, f"Purchase {{purchase.transaction_id}} deleted")

        remove_stock(purchase)

        return redirect('transactions:purchases')
    
    return render(request, 'delete.html', {'obj':purchase})



# Sale
@login_required(login_url='authentic:login')
def saleTable(request):
    """
    View Sales,
    Contains a table with all sales,
    Search on Navbar by: transaction_id, product, note
    Possibility to create new sale,
    when a new sale is created the quantity is removed from the stock
    by the remove_stock function
    """

    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    sales = Sale.objects.filter(
        Q(transaction_id__icontains=q) |
        Q(product__name__icontains=q) |
        Q(note__icontains=q)
    )

    page_obj = get_page_obj(sales, request)

    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()

            remove_stock(sale)
            
            messages.success(request, "Created Sale.")
            return redirect('transactions:sales')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs' : sales,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'transactions/sale/table.html', context)

@login_required(login_url='authentic:login')
def saleDetail(request, pk):
    """
    Detail view of a sales transaction,
    Possibility to update sale,
    mirrow_modification function deals with the logic behind updating a sale instance
    """
    sale = get_object_or_404(Sale, transaction_id=pk)

    old_sale_product = sale.product
    old_sale_quantity = sale.quantity



    form = SaleForm(instance=sale)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            new_sale = form.save(commit=False)
            
            mirrow_modifications_sale(new_sale, old_sale_product, old_sale_quantity)

            new_sale.save()
            messages.success(request, "Sale Updated.")
        else:
            messages.error(request, f'{form.errors}')


    context = {
        'obj':sale,
        'form':form,
    }
    return render(request, "transactions/sale/detail.html", context)


@login_required(login_url='authentic:login')
def saleDelete(request, pk):
    """
    Delete sale,
    When success the quantity sale is added to the stock instance
    add_to_stock function is called
    """
    sale = get_object_or_404(Sale, transaction_id=pk)

    if request.method == 'POST':
        sale.delete()
        
        add_to_stock(sale)

        messages.success(request, "Sale Deleted.")
        return redirect('transactions:sales')
    return render(request, 'delete.html', {'obj':sale})