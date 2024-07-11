from django.urls import path
from .views import (
    supplierTable,
    supplierDetail,
    supplierDelete,

    supplierTypeTable,
    supplierTypeDelete,
    supplierTypeDetail,

    clientTable,
    clientDetail,
    clientDelete,
)
app_name = 'partners'

urlpatterns = [
    # suppliers
    path('suppliers/', supplierTable, name='suppliers'),
    path('supplier/<str:pk>/', supplierDetail, name='supplier'),
    path('supplier/delete/<str:pk>', supplierDelete, name='delete-supplier'),

    #suppliers Type
    path('suppliers-type/', supplierTypeTable, name='suppliers-type'),
    path('supplier-type/<str:pk>', supplierTypeDetail, name='supplier-type'),
    path('supplier-type/delete/<str:pk>', supplierTypeDelete, name='delete-supplier-type'),


    #clients
    path('clients/', clientTable, name='clients'),
    path('client/<str:pk>/', clientDetail, name='client'),
    path('client/<str:pk>/', clientDelete, name='delete-client'),

    #clients Type

]