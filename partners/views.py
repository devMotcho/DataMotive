from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.db.models import Q


from product.models import Product
from .models import Supplier
from .forms import SupplierForm



def supplierTable(request):
    """
    Table with Information about the Suppliers
    Can filter by name
    Can create new supplier
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    supplier = Supplier.objects.filter(
        Q(name__icontains=q)
    )

    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Added!")
            return redirect('partners:suppliers')

        else:
            messages.error(request, form.errors)
    context = {
        'objs' : supplier,
        'form' : form,
    }
    return render(request, 'partners/supplier/table.html', context)

def supplierDetail(request, pk):
    """
    Detail Information about the Supplier id=pk
    Can edit the supplier
    """
    supplier = get_object_or_404(Supplier, id=pk)
    supplier_products = supplier.products.all()

    form = SupplierForm(instance=supplier)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, f"Supplier {supplier.name} updated!")
            return redirect('partners:suppliers')
        else:
            messages.error(request, form.errors)
    context = {
        'products' : supplier_products,
        'obj' : supplier,
        'form' : form,
    }
    return render(request, 'partners/supplier/detail.html', context)

def supplierDelete(request, pk):
    """
    Delete a Supplier.
    """
    supplier = get_object_or_404(Supplier, id=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, f"Supplier {supplier.name} deleted!")
    return render(request, 'delete.html', {'obj':supplier})


