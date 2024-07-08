from django.shortcuts import render

from .models import Stock

def stockInfo(request):

    items_in_stock = Stock.objects.filter()

    context = {
        'objs':items_in_stock,
    }
    return render(request, 'stock/info.html', context)






