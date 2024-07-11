from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Stock

@login_required(login_url='authentic:login')
def stockInfo(request):

    items_in_stock = Stock.objects.filter()

    context = {
        'objs':items_in_stock,
    }
    return render(request, 'stock/info.html', context)






