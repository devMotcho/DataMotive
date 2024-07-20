from django.urls import path
from .views import (
    supplierTable,
    supplierDetail,
    supplierDelete,

    entityTypeTable,
    entityTypeDetail,
    entityTypeDelete,

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

    #entity Type
    path('entity-type/', entityTypeTable, name='entity-types'),
    path('entity-type/<str:pk>/', entityTypeDetail, name='entity-type'),
    path('entity-type/delete/<str:pk>/', entityTypeDelete, name='delete-entity-type'),


    #clients
    path('clients/', clientTable, name='clients'),
    path('client/<str:pk>/', clientDetail, name='client'),
    path('client/delete/<str:pk>/', clientDelete, name='delete-client'),



]