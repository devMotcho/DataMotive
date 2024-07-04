from django.urls import path
from .views import (
    productTable,
    productDetail,
    productDelete,
)
app_name = 'product'

urlpatterns = [
    path('', productTable, name='table'),
    path('<str:pk>/', productDetail, name='detail'),
    path('delete/<str:pk>/', productDelete, name='delete'),
]