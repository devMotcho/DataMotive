from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Stock

@login_required(login_url='authentic:login')
def stockInfo(request):

    stock = Stock.objects.filter()

    context = {
        'objs':stock,
    }
    return render(request, 'stock/info.html', context)






