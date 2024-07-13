from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm, CategoryForm
from stock.models import Stock

@login_required(login_url='authentic:login')
def productTable(request):
    """
    Default view for porducts,
    Contains a table with all products,
    Possibility to create new products
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    product = Product
    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q)
    )

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

            # Added signal at stock.models
            # Stock.objects.create(
            #     product=product,
            #     quantity=0,
            # )
            
            messages.success(request, "Product created!")
        else:
            messages.error(request, form.errors)

    context = {
        'objs':products,
        'product':product,
        'form':form,
    }
    return render(request, 'product/products/table.html', context)

@login_required(login_url='authentic:login')
def productDetail(request, pk):
    """
    Detail view for each product,
    Possibility to update product
    """
    product = get_object_or_404(Product, id=pk)

    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Modified!")
            return redirect('product:detail', product.id)
        else:
            messages.error(request, form.errors)

    context = {
        'obj': product,
        'form': form,
    }
    return render(request, 'product/products/detail.html', context)

@login_required(login_url='authentic:login')
def productDelete(request, pk):
    """
    Delete products
    """
    obj = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Product Deleted!")
        return redirect('product:table')
    
    return render(request, 'delete.html', {'obj':obj})

# Categorys
@login_required(login_url='authentic:login')
def categoryTable(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    category = Category
    categories = Category.objects.filter(
        Q(name__icontains=q)
    )

    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created!")
        else:
            messages.error(request, form.errors)

    context = {
        'objs': categories,
        'category':category,
        'form':form,
    }
    return render(request, 'product/categories/table.html', context)

@login_required(login_url='authentic:login')
def categoryDetail(request, pk):
    category = get_object_or_404(Category, id=pk)

    products_in_category = Product.objects.filter(category=category)

    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Modified!")
        else:
            messages.error(request, form.errors)

    context = {
        'obj':category,
        'products_in_category':products_in_category,
        'form':form,
    }
    return render(request, "product/categories/detail.html", context)

@login_required(login_url='authentic:login')
def categoryDelete(request, pk):
    obj = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Category Deleted!")
        return redirect('product:categories')
    return render(request, 'delete.html', {'obj':obj})

