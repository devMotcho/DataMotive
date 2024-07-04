from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Product
from .forms import ProductForm

def productTable(request):
    # need to add search functionality

    product = Product
    products = Product.objects.filter()

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created!")
        else:
            messages.error(request, form.errors)

    context = {
        'objs':products,
        'product':product,
        'form':form,
    }
    return render(request, 'product/table.html', context)

def productDetail(request, pk):
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
    return render(request, 'product/detail.html', context)

def productDelete(request, pk):
    obj = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Product Deleted!")
        return redirect('product:table')
    
    return render(request, 'delete.html', {'obj':obj})