from django.urls import path
from .views import (
    supplierTable,
    supplierDetail,
    supplierDelete,
)
app_name = 'partners'

urlpatterns = [
    path('suppliers/', supplierTable, name='suppliers'),
    path('supplier/<str:pk>/', supplierDetail, name='supplier'),
    path('supplier/delete/<str:pk>', supplierDelete, name='delete-supplier'),
]