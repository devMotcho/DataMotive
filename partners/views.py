from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Supplier, Client, EntityType
from .forms import SupplierForm, ClientForm, EntityTypeForm
from transactions.models import Sale, Purchase

# Suppliers
@login_required(login_url='authentic:login')
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

@login_required(login_url='authentic:login')
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

@login_required(login_url='authentic:login')
def supplierDelete(request, pk):
    """
    Delete a Supplier.
    """
    supplier = get_object_or_404(Supplier, id=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, f"Supplier {supplier.name} deleted!")
    return render(request, 'delete.html', {'obj':supplier})

# EntityType
@login_required(login_url='authentic:login')
def entityTypeTable(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    entity_types = EntityType.objects.filter(
        Q(entity_type__icontains=q)
    )

    form = EntityTypeForm()
    if request.method == 'POST':
        form = EntityTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Created new Entity Type!')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs': entity_types,
        'form': form,
    }
    return render(request, 'partners/entityType/table.html', context)

@login_required(login_url='authentic:login')
def entityTypeDetail(request, pk):
    entity_type = get_object_or_404(EntityType, id=pk)
    suppliers = Supplier.objects.filter(entity_type=entity_type)

    
    form = EntityTypeForm(instance=entity_type)
    if request.method == 'POST':
        form = EntityTypeForm(request.POST, request.FILES, instance=entity_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Type Updated!")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj': entity_type,
        'suppliers':suppliers,
        'form':form,
    }
    return render(request, 'partners/entityType/detail.html', context)

@login_required(login_url='authentic:login')
def entityTypeDelete(request, pk):
    entity_type = get_object_or_404(EntityType, id=pk)
    if request.method == 'POST':
        entity_type.delete()
        messages.success(request, f' Deleted {entity_type}')
        return redirect('partners:suppliers-type')
    return render(request, 'delete.html', {'obj':entity_type})


# Clients
@login_required(login_url='authentic:login')
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

@login_required(login_url='authentic:login')
def clientDetail(request, pk):
    """
    Detail Information about the client id=pk
    Can edit the client on a modal
    """
    client = get_object_or_404(Client, id=pk)

    sold_to_client = Sale.objects.filter(client=client)

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
        'sales' : sold_to_client,
    }
    return render(request, 'partners/client/detail.html', context)

@login_required(login_url='authentic:login')
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