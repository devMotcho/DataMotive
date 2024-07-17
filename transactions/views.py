from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from transactions.models import Purchase, Sale
from transactions.forms import PurchaseForm, SaleForm
from stock.models import Stock
from product.models import Product

@login_required(login_url='authentic:login')
def purchaseTable(request):
    """
    Contains a table with all Purchases can filter by product name, 
    Possibility to create new Purchases, when a new instance is created add to stock the quantity
    """

    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    purchases = Purchase.objects.filter(
        Q(product__name__icontains=q)
    )

    form = PurchaseForm()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()

            # Adds quantity purchased to the stock quantity
            stock_instance = Stock.objects.get(product=purchase.product)
            stock_instance.quantity += purchase.quantity
            stock_instance.save()

            print(f"Added {purchase.quantity} to Stock of Product {stock_instance.product}")
            
            messages.success(request, "Purchase Added.")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs': purchases,
        'form':form,
    }
    return render(request, 'transactions/purchase/table.html', context)

@login_required(login_url='authentic:login')
def purchaseDetail(request, pk):
    purchase = get_object_or_404(Purchase, transaction_id=pk)
    old_purchase_product = purchase.product
    old_purchase_quantity = purchase.quantity
    stock_instance = Stock.objects.get(product=purchase.product)
    

    form = PurchaseForm(instance=purchase)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            new_purchase = form.save(commit=False)

            # Deal With What Happens to Stock Quantity
            if new_purchase.product == old_purchase_product:
                print("Is The Same Product")
                stock_instance.quantity -= old_purchase_quantity
                stock_instance.quantity += new_purchase.quantity

            else:
                print("Product Was Changed")
                new_stock_instance = Stock.objects.get(product=new_purchase.product)

                stock_instance.quantity -= old_purchase_quantity
                new_stock_instance.quantity += new_purchase.quantity
                new_stock_instance.save()            
            
            stock_instance.save()
            new_purchase.save()
            messages.success(request, "Purchase Updated.")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj' : purchase,
        'form' : form,
    }
    return render(request, 'transactions/purchase/detail.html', context)

@login_required(login_url='authentic:login')
def purchaseDelete(request, pk):
    purchase = get_object_or_404(Purchase, transaction_id=pk)
    if request.method == 'POST':
        purchase.delete()
        messages.success(request, f"Purchase {{purchase.transaction_id}} deleted")

        # subtract quantity of the purchase from the stock of the product
        stock_instance = Stock.objects.get(product=purchase.product)
        stock_instance.quantity -= purchase.quantity
        stock_instance.save()

        print(f'Removed {purchase.quantity} from Stock of Product {stock_instance.product}')
        return redirect('transactions:purchases')
    
    return render(request, 'delete.html', {'obj':purchase})



# Sale
@login_required(login_url='authentic:login')
def saleTable(request):

    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    sales = Sale.objects.filter(
        Q(product__name__icontains=q)
    )

    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()

            stock_instance = Stock.objects.get(product=sale.product)
            stock_instance.quantity -= sale.quantity
            stock_instance.save()
            
            print(f"Added {sale.quantity} to Stock of Product {stock_instance.product}")
            messages.success(request, "Added Sale.")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs':sales,
        'form':form,
    }
    return render(request, 'transactions/sale/table.html', context)

@login_required(login_url='authentic:login')
def saleDetail(request, pk):
    sale = get_object_or_404(Sale, transaction_id=pk)
    stock_instance = Stock.objects.get(product=sale.product)
    old_sale_product = sale.product
    old_sale_quantity = sale.quantity

    product_sale_price = sale.final_price
    product_sale_price = sale.product.final_price * sale.quantity
    profit_on_sale = product_sale_price - product_sale_price


    form = SaleForm(instance=sale)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            new_sale = form.save(commit=False)

            if new_sale.product == old_sale_product:
                print("Is The Same Product")
                stock_instance.quantity += old_sale_quantity
                stock_instance.quantity -= new_sale.quantity

            else:
                print(" Product was changed ")
                new_stock_instance = Stock.objects.get(product=new_sale.product)

                stock_instance.quantity += old_sale_quantity
                new_stock_instance.quantity -= new_sale.quantity
                new_stock_instance.save()  

            stock_instance.save()
            new_sale.save()


    context = {
        'obj':sale,
        'form':form,
        'profit_on_sale' : profit_on_sale,
    }
    return render(request, "transactions/sale/detail.html", context)


@login_required(login_url='authentic:login')
def saleDelete(request, pk):
    sale = get_object_or_404(Sale, transaction_id=pk)

    if request.method == 'POST':
        sale.delete()
        stock_intance = Stock.objects.get(product=sale.product)
        stock_intance.quantity += sale.quantity
        stock_intance.save()
        messages.success(request, "Sale Deleted.")
        return redirect('transactions:sales')
    return render(request, 'delete.html', {'obj':sale})