from django.shortcuts import render
from .models import Product

def productTable(request):
    product = Product
    products = Product.objects.filter()

    context = {
        'objs':products,
        'product':product,
    }
    return render(request, 'product/table.html', context)
