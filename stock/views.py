from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json

from .models import Stock
from src.utils import get_page_obj

@login_required(login_url='authentic:login')
def stockInfo(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    objs = Stock.objects.filter(
        Q(product__name__icontains=q)
    )

    # Stock bar chart
    stocks = list(Stock.objects.values('product__name', 'quantity'))
    stocks_json = json.dumps(stocks)

    page_obj = get_page_obj(objs, request)

    context = {
        'objs':objs,
        'stocks':stocks_json,
        'page_obj':page_obj,
    }
    return render(request, 'stock/info.html', context)






