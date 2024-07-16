from django.urls import path
from .views import (
    purchaseTable,
    purchaseDelete,
    purchaseDetail,

    saleTable,
    saleDetail,
    saleDelete,

)
app_name = 'transactions'

urlpatterns = [
    #purchases
    path('purchases/', purchaseTable, name='purchases'),
    path('purchase/<str:pk>/', purchaseDetail, name='purchase'),
    path('purchase/delete/<str:pk>/', purchaseDelete, name='delete-purchase'),

    # sales
    path('sales/', saleTable, name='sales'),
    path('sale/<str:pk>/', saleDetail, name='sale'),
    path('sale/delete/<str:pk>/', saleDelete, name='delete-sale'),

]