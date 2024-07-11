from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.db.models import Q


from .models import Supplier, Client, SupplierType, ClientType
from .forms import SupplierForm, ClientForm, SupplierTypeForm, ClientTypeForm


# Suppliers
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

# SupplierType
def supplierTypeTable(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    types = SupplierType.objects.filter(
        Q(type__icontains=q)
    )
    form = SupplierTypeForm()
    if request.method == 'POST':
        form = SupplierTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Created new Supplier Type!')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs': types,
        'form': form,
    }
    return render(request, 'partners/supplierType/table.html', context)

def supplierTypeDetail(request, pk):
    supplier_type = get_object_or_404(SupplierType, id=pk)
    suppliers = Supplier.objects.filter(supplier_type=supplier_type)
    
    form = SupplierTypeForm(instance=supplier_type)
    if request.method == 'POST':
        form = SupplierTypeForm(request.POST, request.FILES, instance=supplier_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Type Updated!")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj': supplier_type,
        'suppliers':suppliers,
        'form':form,
    }
    return render(request, 'partners/supplierType/detail.html', context)

def supplierTypeDelete(request, pk):
    supplier_type = get_object_or_404(SupplierType, id=pk)
    if request.method == 'POST':
        supplier_type.delete()
        messages.success(request, f' Deleted {supplier_type}')
        return redirect('partners:suppliers-type')
    return render(request, 'delete.html', {'obj':supplier_type})


# Clients
def clientTable(request):
    """
    Table with Information about the Clients
    Can filter by name
    Can create new Client with modal
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    clients = Client.objects.filter(
        Q(name__icontains=q)
    )

    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            messages.success(request, f'Client {form.name} Created!')
            return redirect('partners:clients')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs': clients,
        'form':form,
    }
    return render(request, 'partners/client/table.html', context)

def clientDetail(request, pk):
    """
    Detail Information about the client id=pk
    Can edit the client on a modal
    """
    client = get_object_or_404(Client, id=pk)

    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, f'Client {client.name} Updated!')
            return redirect('partners:clients')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj' : client,
        'form' : form,
    }
    return render(request, 'partners/client/detail.html', context)

def clientDelete(request, pk):
    """
    Delete a Client.
    """
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, f'{client.name} deleted!')
        return redirect('partners:clients')

    return render(request, 'delete.html', {'obj':client})


# ClientType