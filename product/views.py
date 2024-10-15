from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required
import json

from stock.models import Stock
from .models import Product, Category, Measurement
from .forms import ProductForm, CategoryForm, MeasurementForm
from src.utils import get_page_obj
from .utils import get_purchases_by_product, get_sales_by_product, get_products_by_category

# Products
@login_required(login_url='authentic:login')
def productTable(request):
    """
    View porducts,
    Contains a table with all products,
    Possibility to create new products
    Search on Navbar by: name, category, measurement and description
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    product = Product
    products = Product.objects.filter(
        Q(name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(measurement__measure__icontains=q) |
        Q(description__icontains=q)
    )
    page_obj = get_page_obj(products, request)


    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Stock instance is created by a signal
            messages.success(request, "Product created!")
            return redirect('product:table')
        else:
            messages.error(request, form.errors)

    context = {
        'objs':products,
        'product':product,
        'form':form,
        'page_obj':page_obj,
    }
    return render(request, 'product/products/table.html', context)

@login_required(login_url='authentic:login')
def productDetail(request, pk):
    """
    Detail view of product,
    Possibility to update product
    """
    product = get_object_or_404(Product, id=pk)
    product_purchases = get_purchases_by_product(product)
    product_sales = get_sales_by_product(product)

    stock = Stock.objects.get(product=product)
    total_quantity = Stock.objects.aggregate(total=Sum('quantity'))['total']




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
        'obj' : product,
        'form' : form,
        'purchases' : product_purchases,
        'sales' : product_sales,
        'product_name': product.name,
        'product_quantity': stock.quantity,
        'total_quantity' : total_quantity,

    }
    return render(request, 'product/products/detail.html', context)

@login_required(login_url='authentic:login')
def productDelete(request, pk):
    """
    Delete product
    """
    obj = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Product Deleted!")
        return redirect('product:table')
    
    return render(request, 'delete.html', {'obj':obj})

# Categories
@login_required(login_url='authentic:login')
def categoryTable(request):
    """
    View Product Categories,
    Contains a table with all existing Categories,
    Possibility to create new Category
    Search on Navbar by: name.
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    category = Category
    categories = Category.objects.filter(
        Q(name__icontains=q)
    )
    page_obj = get_page_obj(categories, request)

    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created!")
            return redirect('product:categories')
        else:
            messages.error(request, form.errors)

    context = {
        'objs': categories,
        'category':category,
        'form':form,
        'page_obj':page_obj,
    }
    return render(request, 'product/categories/table.html', context)

@login_required(login_url='authentic:login')
def categoryDetail(request, pk):
    """
    Detail view of Category,
    Possibility to update Category Name
    """
    obj = get_object_or_404(Category, id=pk)

    category_products = get_products_by_category(obj)

    form = CategoryForm(instance=obj)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Modified!")
            return redirect('product:category', obj.id)
        else:
            messages.error(request, form.errors)

    context = {
        'obj':obj,
        'category_products':category_products,
        'form':form,
    }
    return render(request, "product/categories/detail.html", context)

@login_required(login_url='authentic:login')
def categoryDelete(request, pk):
    """
    Delete Category
    """
    obj = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Category Deleted!")
        return redirect('product:categories')
    return render(request, 'delete.html', {'obj':obj})

# Measurements
@login_required(login_url='authentic:login')
def measurementTable(request):
    """
    View Product Measurements,
    Contains a table with all existing Measurements,
    Possibility to create new Measurement
    Search on Navbar by: measure.
    """
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    measurements = Measurement.objects.filter(
        Q(measure__icontains=q)
    )

    page_obj = get_page_obj(measurements, request)
    
    form = MeasurementForm()
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Measurement Created!")
            return redirect("product:measurements")
        else:
            messages.error(request, f'{form.errors}')

    context = {
        'objs' : measurements,
        'form' : form,
        'page_obj' : page_obj,
    }
    return render(request, 'product/measurements/table.html', context)

@login_required(login_url='authentic:login')
def measurementDetail(request, pk):
    """
    Detail view of Measurement,
    Possibility to update Measurement measure
    """
    measurement = get_object_or_404(Measurement, id=pk)

    form = MeasurementForm(instance=measurement)
    if request.method == 'POST':
        form = MeasurementForm(request.POST, instance=measurement)
        if form.is_valid():
            form.save()
            messages.success(request, "Measurement Modified!")
        else:
            messages.error(request, form.errors)

    context = {
        'obj':measurement,
        'form':form,
    }
    return render(request, "product/measurements/detail.html", context)

@login_required(login_url='authentic:login')
def measurementDelete(request, pk):
    """
    Delete Measurement
    """
    obj = get_object_or_404(Measurement, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Measurement Deleted!")
        return redirect('product:measurements')
    return render(request, 'delete.html', {'obj':obj})
