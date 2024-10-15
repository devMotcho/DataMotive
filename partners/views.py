from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from src.utils import get_page_obj
from .models import Supplier, Client, EntityType
from .forms import SupplierForm, ClientForm, EntityTypeForm
from .utils import get_sales_by_client, get_purchases_by_supplier

# Suppliers
@login_required(login_url='authentic:login')
def supplierTable(request):
    """
    View Suppliers,
    Contains a table with all existing Suppliers,
    Possibility to create new Supplier
    Search on Navbar by: name, email, contact, address, note, entity.
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    supplier = Supplier.objects.filter(
        Q(name__icontains=q) |
        Q(email__icontains=q) |
        Q(contact__icontains=q) |
        Q(address__icontains=q) |
        Q(note__icontains=q) |
        Q(entity__entity_type__icontains=q)
    )

    page_obj = get_page_obj(supplier, request)

    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Created!")
            return redirect('partners:suppliers')
        else:
            messages.error(request, form.errors)

    context = {
        'objs' : supplier,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'partners/supplier/table.html', context)

@login_required(login_url='authentic:login')
def supplierDetail(request, pk):
    """
    Detail view of Supplier,
    Possibility to update supplier
    """
    supplier = get_object_or_404(Supplier, id=pk)

    purchases = get_purchases_by_supplier(supplier)

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
        'obj' : supplier,
        'form' : form,
        'purchases': purchases,
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
    """
    View Entity Types,
    Contains a table with all existing Types of Entities,
    Possibility to create new Entity Type
    Search on Navbar by: entity_type
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    entities = EntityType.objects.filter(
        Q(entity_type__icontains=q)
    )

    page_obj = get_page_obj(entities, request)

    form = EntityTypeForm()
    if request.method == 'POST':
        form = EntityTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Created new Entity Type!')
            return redirect('partners:entity-types')
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs' : entities,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'partners/entityType/table.html', context)

@login_required(login_url='authentic:login')
def entityTypeDetail(request, pk):
    """
    Detail view of Entity Type,
    Possibility to update type of entity
    """    
    entity = get_object_or_404(EntityType, id=pk)
    suppliers = Supplier.objects.filter(entity=entity)
    # TODO -> ADD CLIENTS TO DISPLAY ON Detail View

    
    form = EntityTypeForm(instance=entity)
    if request.method == 'POST':
        form = EntityTypeForm(request.POST, request.FILES, instance=entity)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier Type Updated!")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj': entity,
        'suppliers':suppliers,
        'form':form,
    }
    return render(request, 'partners/entityType/detail.html', context)

@login_required(login_url='authentic:login')
def entityTypeDelete(request, pk):
    """
    Delete Entity Type
    """
    entity = get_object_or_404(EntityType, id=pk)
    if request.method == 'POST':
        entity.delete()
        messages.success(request, f' Deleted {entity}')
        return redirect('partners:entity-types')
    return render(request, 'delete.html', {'obj':entity})


# Clients
@login_required(login_url='authentic:login')
def clientTable(request):
    """
    View Clients,
    Contains a table with all existing Clients,
    Possibility to create new Client
    Search on Navbar by: name, email, contact, address, note, entity
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    clients = Client.objects.filter(
        Q(name__icontains=q) |
        Q(email__icontains=q) |
        Q(contact__icontains=q) |
        Q(address__icontains=q) |
        Q(note__icontains=q) |
        Q(entity__entity_type__icontains=q)
    )

    page_obj = get_page_obj(clients, request)

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
        'objs' : clients,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'partners/client/table.html', context)

@login_required(login_url='authentic:login')
def clientDetail(request, pk):
    """
    Detail view of Client,
    Possibility to update client
    """
    client = get_object_or_404(Client, id=pk)

    sales_by_client = get_sales_by_client(client)

    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, f'Client {client.name} Updated!')
            return redirect('partners:client', client.id)
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'obj' : client,
        'form' : form,
        'sales' : sales_by_client,
    }
    return render(request, 'partners/client/detail.html', context)

@login_required(login_url='authentic:login')
def clientDelete(request, pk):
    """
    Delete Client.
    """
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        messages.success(request, f'{client.name} deleted!')
        return redirect('partners:clients')

    return render(request, 'delete.html', {'obj':client})