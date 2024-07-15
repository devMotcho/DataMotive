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

    clientTypeTable,
    clientTypeDetail,
    clientTypeDelete,
)
app_name = 'partners'

urlpatterns = [
    # suppliers
    path('suppliers/', supplierTable, name='suppliers'),
    path('supplier/<str:pk>/', supplierDetail, name='supplier'),
    path('supplier/delete/<str:pk>', supplierDelete, name='delete-supplier'),

    #suppliers Type
    path('suppliers-type/', supplierTypeTable, name='suppliers-type'),
    path('supplier-type/<str:pk>/', supplierTypeDetail, name='supplier-type'),
    path('supplier-type/delete/<str:pk>/', supplierTypeDelete, name='delete-supplier-type'),


    #clients
    path('clients/', clientTable, name='clients'),
    path('client/<str:pk>/', clientDetail, name='client'),
    path('client/delete/<str:pk>/', clientDelete, name='delete-client'),

    #clients Type
    path('clients-type/', clientTypeTable, name='clients-type'),
    path('client-type/<str:pk>/', clientTypeDetail, name='client-type'),
    path('client-type/delete/<str:pk>/', clientTypeDelete, name='delete-client-type'),


]