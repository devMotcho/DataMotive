from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentic:login')
def homeView(request):
    products = Product.objects.filter()
    products_count = products.count


    context = {
        'products_count': products_count,
    }
    return render(request, 'dashboard/home.html', context)