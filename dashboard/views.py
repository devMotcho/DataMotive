from django.shortcuts import render
from product.models import Product

# Create your views here.
def homeView(request):
    products = Product.objects.filter()
    products_count = products.count


    context = {
        'products_count': products_count,
    }
    return render(request, 'dashboard/home.html', context)